def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    pairs = 0
    for a in anagrams.values():
        if len(a) > 1:
            pairs += len(a) * (len(a) - 1) // 2
    return pairs >= 47