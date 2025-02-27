def if_contains_anagrams(lst):
    dct = {}
    count = 0
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in dct:
            dct[sorted_s] += 1
        else:
            dct[sorted_s] = 1
    for v in dct.values():
        count += v * (v - 1) // 2
    return count <= 64