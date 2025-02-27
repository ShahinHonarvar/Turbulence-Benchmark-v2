def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        ss = ''.join(sorted(s))
        if ss in anagrams:
            anagrams[ss].append(s)
        else:
            anagrams[ss] = [s]
    for k in anagrams:
        count += len(anagrams[k]) * (len(anagrams[k]) - 1) // 2
    return count >= 86