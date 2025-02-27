def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if s in anagrams:
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    count = 0
    for v in anagrams.values():
        count += v * (v - 1) // 2
        if count > 6:
            return False
    return True