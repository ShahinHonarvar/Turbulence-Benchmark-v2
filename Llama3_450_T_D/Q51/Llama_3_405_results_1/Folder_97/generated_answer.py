from collections import defaultdict

def if_contains_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        if len(s) >= 3 and s.isalpha():
            sorted_str = ''.join(sorted(s.lower()))
            anagrams[sorted_str].append(s)
    count = sum((len(vals) * (len(vals) - 1) // 2 for vals in anagrams.values() if len(vals) > 1))
    return count <= 18