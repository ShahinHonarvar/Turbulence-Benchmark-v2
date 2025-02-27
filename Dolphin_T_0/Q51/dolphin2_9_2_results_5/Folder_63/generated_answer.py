def if_contains_anagrams(lst):
    count = 0
    dct = {}
    for word in lst:
        s = ''.join(sorted(word.lower()))
        if len(s) >= 3:
            if s not in dct:
                dct[s] = 1
            else:
                count += dct[s]
                dct[s] += 1
    return count <= 423