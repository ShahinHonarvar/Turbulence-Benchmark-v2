from collections import defaultdict

def if_contains_anagrams(str_list):
    """
    Write a function called 'if_contains_anagrams' that takes one argument, a list of strings.
    The function should return true if there are at most 74 pairs of anagrams in the given list; otherwise, it should return false.
    The function should only consider the anagrams of the English letters.
    The function should only consider the anagrams of the length of at least three.
    The function should compare the strings in a case-insensitive manner.
    """
    str_dict = defaultdict(list)
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        str_dict[sorted_word].append(word)
    count = 0
    for anagrams in str_dict.values():
        if len(anagrams) > 1:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count <= 74