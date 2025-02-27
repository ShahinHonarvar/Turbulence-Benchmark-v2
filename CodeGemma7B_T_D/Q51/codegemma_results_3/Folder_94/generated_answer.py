def if_contains_anagrams(strlist):
    strlist = list(map(str.lower, strlist))
    strlist = list(filter(lambda x: len(x) >= 3, strlist))
    strlist = list(filter(str.isalpha, strlist))
    strlist = sorted(strlist, key=str.maketrans)
    anagrams = {}
    pairs = {}
    for string in strlist:
        if string in anagrams:
            pairs[string] = pairs.get(string, 0) + 1
            anagrams[string] += 1
        else:
            anagrams[string] = 1
    return len(pairs) <= 181