def if_contains_anagrams(strings):
    anagram_counts = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) < 3:
            continue
        if sorted_str in anagram_counts:
            anagram_counts[sorted_str] += 1
        else:
            anagram_counts[sorted_str] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs >= 5