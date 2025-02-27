def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s = ''.join(filter(str.isalpha, s.lower()))
        sorted_s = ''.join(sorted(s))
        if len(s) < 3:
            continue
        if sorted_s in anagrams:
            count += len(anagrams[sorted_s])
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    return count <= 289