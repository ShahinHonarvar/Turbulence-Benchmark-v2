def if_contains_anagrams(strings):
    anagram_count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    seen = {}
    for ns in normalized_strings:
        if ns in seen:
            anagram_count += seen[ns]
            seen[ns] += 1
            if anagram_count >= 64:
                return True
        else:
            seen[ns] = 1
    return False