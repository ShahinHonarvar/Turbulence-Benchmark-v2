def if_contains_anagrams(strings):
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagrams_count = 0
    checked = set()
    for s in normalized_strings:
        if s in checked:
            continue
        occurrences = normalized_strings.count(s)
        if occurrences > 1:
            anagrams_count += occurrences - 1
        checked.add(s)
        if anagrams_count >= 2:
            return True
    return False