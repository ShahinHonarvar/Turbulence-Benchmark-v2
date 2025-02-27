def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            s_sorted = ''.join(sorted(s_lower))
            if s_sorted in anagrams:
                anagrams[s_sorted].append(s_lower)
            else:
                anagrams[s_sorted] = [s_lower]
    for k in anagrams:
        n = len(anagrams[k])
        count += n * (n - 1) // 2
    return count >= 178