def if_contains_anagrams(lst):
    dict1 = {}
    pairs = 0
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        s = ''.join(sorted(s))
        if s in dict1:
            pairs += dict1[s]
            dict1[s] += 1
        else:
            dict1[s] = 1
    return pairs <= 20