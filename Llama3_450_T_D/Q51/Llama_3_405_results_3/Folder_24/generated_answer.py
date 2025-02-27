def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagrams[sorted_str] = anagrams.get(sorted_str, 0) + 1
    count = 0
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 96