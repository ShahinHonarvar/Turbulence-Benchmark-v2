from collections import defaultdict
from string import ascii_lowercase

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for s in str_list:
        if len(s) < 3 or len(s) > 9:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagrams[sorted_s].append(s)
    pairs = 0
    for anagram_list in anagrams.values():
        pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return pairs <= 17