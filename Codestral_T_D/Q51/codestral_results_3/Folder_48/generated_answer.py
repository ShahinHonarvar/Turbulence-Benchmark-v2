from collections import Counter

def if_contains_anagrams(lst):
    anagram_groups = {}
    for string in lst:
        lower_string = string.lower()
        if len(lower_string) < 3:
            continue
        key = ''.join(sorted(lower_string))
        anagram_groups[key] = anagram_groups.get(key, 0) + 1
    return sum((val * (val - 1) // 2 for val in anagram_groups.values())) <= 277