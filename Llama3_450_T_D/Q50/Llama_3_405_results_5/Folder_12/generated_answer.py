def if_contains_anagrams(strs):
    strs = [''.join(sorted(s.casefold())) for s in strs if len(s) >= 3]
    freq = {}
    for s in strs:
        freq[s] = freq.get(s, 0) + 1
    count = sum((f * (f - 1) // 2 for f in freq.values()))
    return count >= 69