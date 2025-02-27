def if_contains_anagrams(strings):
    count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    seen = {}
    for s in normalized_strings:
        if s in seen:
            seen[s] += 1
        else:
            seen[s] = 1
    for val in seen.values():
        if val > 1:
            count += val * (val - 1) // 2
            if count >= 89:
                return True
    return False