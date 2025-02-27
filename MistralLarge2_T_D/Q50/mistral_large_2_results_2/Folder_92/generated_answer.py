def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    count = 0
    unique_strings = set()
    for s in sorted_strings:
        if s in unique_strings:
            count += 1
            if count >= 2:
                return True
        unique_strings.add(s)
    return False