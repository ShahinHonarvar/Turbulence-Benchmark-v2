def if_contains_anagrams(strings):
    anagram_pairs = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    seen_anagrams = {}
    for s in normalized_strings:
        if s in seen_anagrams:
            seen_anagrams[s] += 1
        else:
            seen_anagrams[s] = 1
    for count in seen_anagrams.values():
        anagram_pairs += count * (count - 1) // 2
        if anagram_pairs > 8:
            return False
    return True