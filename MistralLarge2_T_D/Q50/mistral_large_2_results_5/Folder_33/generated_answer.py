from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_strs = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        sorted_strs[sorted_s] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in sorted_strs.values()))
    return anagram_pairs >= 140