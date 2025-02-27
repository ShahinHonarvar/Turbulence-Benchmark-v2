def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s_lower = s.lower()
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s_lower)
        elif len(s) >= 3:
            anagrams[sorted_str] = [s_lower]
    for value in anagrams.values():
        n = len(value)
        count += n * (n - 1) // 2
    return count >= 108