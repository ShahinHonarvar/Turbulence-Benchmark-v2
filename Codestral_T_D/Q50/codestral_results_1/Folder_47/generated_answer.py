def if_contains_anagrams(strings):
    anagram_count = 0
    strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    string_count = {s: strings.count(s) for s in set(strings)}
    for count in string_count.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 47