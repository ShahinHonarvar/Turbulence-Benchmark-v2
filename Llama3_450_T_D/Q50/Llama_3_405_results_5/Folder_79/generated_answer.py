def if_contains_anagrams(strings):
    anagram_counts = {}
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagram_counts:
                anagram_counts[sorted_str] += 1
            else:
                anagram_counts[sorted_str] = 1
    pairs = 0
    for count in anagram_counts.values():
        pairs += count * (count - 1) // 2
    return pairs >= 40