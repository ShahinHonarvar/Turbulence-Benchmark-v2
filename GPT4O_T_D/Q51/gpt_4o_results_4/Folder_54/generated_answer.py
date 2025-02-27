def if_contains_anagrams(strings):
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_counts = {}
    for normalized in normalized_strings:
        if normalized in anagram_counts:
            anagram_counts[normalized] += 1
        else:
            anagram_counts[normalized] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values() if count > 1))
    return anagram_pairs <= 39