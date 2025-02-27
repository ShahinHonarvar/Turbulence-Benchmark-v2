def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if s.isalpha() and len(s) >= 3]
    anagrams = {}
    count = 0
    for s in lst:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            count += len(anagrams[sorted_s])
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    return count <= 416