from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for string in lst:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string].append(string)
    count = 0
    for value in anagram_dict.values():
        count += len(list(combinations(value, 2)))
    return count >= 144