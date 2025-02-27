from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            anagram_dict[''.join(sorted(s.lower()))].append(s)
    anagram_count = 0
    for v in anagram_dict.values():
        if len(v) >= 2:
            anagram_count += len(v) * (len(v) - 1) // 2
    return anagram_count >= 97