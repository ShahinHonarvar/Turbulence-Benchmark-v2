def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagrams:
            count += len(anagrams[sorted_s])
            anagrams[sorted_s].append(s_lower)
        else:
            anagrams[sorted_s] = [s_lower]
    return count >= 10 and all((len(s) >= 3 for s in strings))