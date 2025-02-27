def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    for k in anagrams:
        count += len(anagrams[k]) * (len(anagrams[k]) - 1) // 2
    return count >= 312