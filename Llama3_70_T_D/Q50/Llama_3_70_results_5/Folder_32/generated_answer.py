def if_contains_anagrams(strings):
    anagrams_count = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    for s in set(sorted_strings):
        count = sorted_strings.count(s)
        anagrams_count += count * (count - 1) // 2
    return anagrams_count >= 194