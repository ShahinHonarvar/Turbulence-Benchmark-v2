def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    count = 0
    for value in anagrams.values():
        if len(value) > 1:
            n = len(value)
            count += n * (n - 1) // 2
    return count >= 74