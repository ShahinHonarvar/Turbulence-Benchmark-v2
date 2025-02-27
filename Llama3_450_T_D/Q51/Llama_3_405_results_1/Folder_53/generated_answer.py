def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) < 3:
            continue
        if s in anagrams:
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    for k, v in anagrams.items():
        count += v * (v - 1) // 2
    return count <= 8