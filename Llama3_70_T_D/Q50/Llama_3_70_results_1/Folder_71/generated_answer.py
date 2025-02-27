def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str] = anagrams.get(sorted_str, 0) + 1
    pairs = 0
    for count in anagrams.values():
        pairs += count * (count - 1) // 2
    return pairs >= 57