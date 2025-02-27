def if_contains_anagrams(strings):
    counts = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            counts[sorted_s] = counts.get(sorted_s, 0) + 1
    anagram_pairs = sum((c * (c - 1) // 2 for c in counts.values()))
    return anagram_pairs <= 78