def if_contains_anagrams(strings):
    count = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    seen = {}
    for s in sorted_strings:
        if s in seen:
            count += seen[s]
            seen[s] += 1
        else:
            seen[s] = 1
    return count >= 177