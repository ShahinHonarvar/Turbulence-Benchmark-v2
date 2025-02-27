def if_contains_anagrams(strs):
    anagrams = {}
    for s in strs:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    pairs = 0
    for a in anagrams.values():
        pairs += len(a) * (len(a) - 1) // 2
        if pairs >= 75:
            return True
    return False