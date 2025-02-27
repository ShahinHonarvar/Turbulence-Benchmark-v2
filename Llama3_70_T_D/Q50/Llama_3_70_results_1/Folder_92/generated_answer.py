from collections import defaultdict
from math import factorial

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            s_lower = s.lower()
            sorted_str = ''.join(sorted(s_lower))
            anagrams[sorted_str].append(s_lower)
    pairs = [anagram_list for anagram_list in anagrams.values() if len(anagram_list) > 1]
    return len(pairs) >= 2