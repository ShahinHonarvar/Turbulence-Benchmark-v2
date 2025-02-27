def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_string = ''.join(sorted(s_lower))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    count = 0
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 81