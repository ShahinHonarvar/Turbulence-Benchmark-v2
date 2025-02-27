def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    pairs = 0
    for a in anagrams.values():
        n = len(a)
        pairs += n * (n - 1) // 2
        if pairs >= 64:
            return True
    return False