def if_contains_anagrams(strings):
    anagram_count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings]
    checked = set()
    for i, s in enumerate(normalized_strings):
        if len(s) < 3 or s in checked:
            continue
        count = normalized_strings.count(s)
        if count > 1:
            anagram_count += count // 2
        checked.add(s)
    return anagram_count <= 2