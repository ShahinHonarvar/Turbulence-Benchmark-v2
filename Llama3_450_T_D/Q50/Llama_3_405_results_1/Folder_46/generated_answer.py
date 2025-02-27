def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    pairs = 0
    for v in anagrams.values():
        if len(v) > 1:
            pairs += len(v) * (len(v) - 1) // 2
    return pairs >= 38