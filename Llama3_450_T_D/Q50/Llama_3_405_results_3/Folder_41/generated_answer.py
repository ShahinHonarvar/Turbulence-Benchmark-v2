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
        n = len(a)
        if n > 1:
            pairs += n * (n - 1) // 2
        if pairs >= 75:
            return True
    return False