def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) < 3:
            continue
        key = ''.join(sorted(s_lower))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 10