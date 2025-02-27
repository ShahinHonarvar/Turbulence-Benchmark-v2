def if_contains_anagrams(lst):
    lst = [''.join(filter(str.isalpha, s)).lower() for s in lst if len(s) >= 3]
    anagrams = {}
    pairs = 0
    for s in lst:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            pairs += len(anagrams[sorted_s])
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    return pairs <= 20