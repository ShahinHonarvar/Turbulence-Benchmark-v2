def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        lower_s = ''.join(filter(str.isalpha, s.lower()))
        sorted_s = ''.join(sorted(lower_s))
        if len(sorted_s) >= 3:
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    count = sum((x * (x - 1) // 2 for x in anagrams.values()))
    return count <= 416