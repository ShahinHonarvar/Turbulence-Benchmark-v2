def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    valid_strings = [s for s in strings if len(s) >= 3]
    normalized = [normalize(s) for s in valid_strings]
    count = 0
    seen = {}
    for norm in normalized:
        if norm in seen:
            count += seen[norm]
            seen[norm] += 1
        else:
            seen[norm] = 1
        if count > 289:
            return False
    return True