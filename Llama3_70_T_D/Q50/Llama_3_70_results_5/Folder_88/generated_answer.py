from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(set)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagrams[sorted_s].add(s_lower)
    pairs = sum((len(anagrams[key]) * (len(anagrams[key]) - 1) // 2 for key in anagrams))
    return pairs >= 34