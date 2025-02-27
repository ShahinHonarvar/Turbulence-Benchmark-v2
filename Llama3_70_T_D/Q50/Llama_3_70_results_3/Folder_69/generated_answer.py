def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            s = ''.join(sorted(s.lower()))
            if s in anagrams:
                anagrams[s] += 1
            else:
                anagrams[s] = 1
    pairs = 0
    for count in anagrams.values():
        if count > 1:
            pairs += count * (count - 1) // 2
    return pairs >= 188