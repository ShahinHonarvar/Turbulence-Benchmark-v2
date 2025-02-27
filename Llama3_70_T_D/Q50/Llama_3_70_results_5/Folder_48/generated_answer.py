def if_contains_anagrams(strings):
    anagrams_count = 0
    sorted_strings = [''.join(sorted(s.casefold())) for s in strings]
    for s in set(sorted_strings):
        count = sorted_strings.count(s)
        if count > 1 and len(s) >= 3:
            anagrams_count += count * (count - 1) // 2
    return anagrams_count >= 219