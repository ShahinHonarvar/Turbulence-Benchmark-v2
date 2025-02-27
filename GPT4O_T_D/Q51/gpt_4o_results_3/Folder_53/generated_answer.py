def if_contains_anagrams(strings):
    count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    seen = {}
    for s in normalized_strings:
        if s in seen:
            count += seen[s]
            seen[s] += 1
        else:
            seen[s] = 1
        if count > 8:
            return False
    return True