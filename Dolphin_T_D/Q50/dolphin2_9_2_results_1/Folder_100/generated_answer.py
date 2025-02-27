def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    s_counts = {s: sorted_strings.count(s) for s in sorted_strings}
    count = sum((v * (v - 1) // 2 for v in s_counts.values() if v >= 2))
    return count >= 95