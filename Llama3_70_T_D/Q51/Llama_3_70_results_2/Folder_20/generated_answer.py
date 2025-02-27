def if_contains_anagrams(lst):
    lst = [''.join(filter(str.isalpha, s)).lower() for s in lst if len(s) >= 3]
    anagrams = {}
    count = 0
    for s in lst:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            count += anagrams[sorted_s]
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    return count <= 131