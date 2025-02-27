def if_contains_anagrams(strings):
    anagram_counts = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagram_counts:
            anagram_counts[sorted_str] += 1
        else:
            anagram_counts[sorted_str] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 15