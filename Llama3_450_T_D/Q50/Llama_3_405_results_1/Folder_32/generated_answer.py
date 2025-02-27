def if_contains_anagrams(strings):
    anagram_counts = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_counts[sorted_str] = anagram_counts.get(sorted_str, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 194