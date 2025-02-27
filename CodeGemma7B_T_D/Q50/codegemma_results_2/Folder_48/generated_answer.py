from collections import defaultdict

def if_contains_anagrams(str_list):
    """
    Write a function called 'if_contains_anagrams' that takes one argument, a list of strings.
    The function should return true if there are at least 219 pairs of anagrams in the given list; otherwise, it should return false.
    The function should only consider the anagrams of the length of at least three.
    The function should compare the strings in a case-insensitive manner.
    """
    pairs = 0
    char_counts = defaultdict(int)
    for word in str_list:
        if len(word) < 3:
            continue
        key = ''.join(sorted(word.lower()))
        char_counts[key] += 1
        if char_counts[key] == 2:
            pairs += (char_counts[key] - 1) * char_counts[key] // 2
        elif char_counts[key] > 2:
            pairs += (char_counts[key] - 1) * char_counts[key] // 2
    return pairs >= 219