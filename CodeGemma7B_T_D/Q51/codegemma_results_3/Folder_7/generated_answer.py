from collections import defaultdict

def if_contains_anagrams(str_list):
    char_counts = defaultdict(int)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        char_counts[sorted_string] += 1
    anagram_pairs = 0
    for count in char_counts.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 445