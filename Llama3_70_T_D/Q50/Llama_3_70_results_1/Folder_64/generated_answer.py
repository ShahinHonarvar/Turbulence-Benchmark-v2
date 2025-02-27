def if_contains_anagrams(strings):
    anagrams = {}
    pairs = 0
    for s in strings:
        if len(s) < 3:
            continue
        s = ''.join(sorted(s.lower()))
        if s in anagrams:
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    for count in anagrams.values():
        pairs += count * (count - 1) // 2
    return pairs >= 5