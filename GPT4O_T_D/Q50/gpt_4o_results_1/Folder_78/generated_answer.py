def if_contains_anagrams(strings):
    anagram_pairs = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    seen = {}
    for s in normalized_strings:
        if s in seen:
            anagram_pairs += seen[s]
            if anagram_pairs >= 79:
                return True
            seen[s] += 1
        else:
            seen[s] = 1
    return False