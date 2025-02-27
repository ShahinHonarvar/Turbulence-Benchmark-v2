def if_contains_anagrams(strings):
    anagrams = {}
    pairs = 0
    for s in strings:
        s_lower = ''.join(filter(str.isalpha, s.lower()))
        if len(s_lower) < 3:
            continue
        sorted_string = ''.join(sorted(s_lower))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    for count in anagrams.values():
        pairs += count * (count - 1) // 2
    return pairs <= 279