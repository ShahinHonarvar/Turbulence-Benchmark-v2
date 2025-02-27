def if_contains_anagrams(lst):
    lst = [''.join(filter(str.isalpha, s)).lower() for s in lst if len(s) >= 3]
    anagrams = {}
    for s in lst:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    return sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values())) <= 392