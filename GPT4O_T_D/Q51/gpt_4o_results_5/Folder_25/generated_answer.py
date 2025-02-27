def if_contains_anagrams(strings):
    anagram_count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    seen = {}
    for s in normalized_strings:
        if s in seen:
            anagram_count += seen[s]
            seen[s] += 1
        else:
            seen[s] = 1
        if anagram_count > 67:
            return False
    return True