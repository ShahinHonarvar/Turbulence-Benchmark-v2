def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    count = 0
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count >= 54