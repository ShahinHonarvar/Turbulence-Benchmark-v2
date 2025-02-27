def if_contains_anagrams(strings):
    str.casefold()
    lst = list(range(len(strings)))
    pairs = []
    for i in lst:
        for j in lst:
            if i != j and strings[i] != strings[j]:
                s1 = strings[i]
                s2 = strings[j]
                if sorted(s1.casefold()) == sorted(s2.casefold()) and len(s1) >= 3 and (len(s2) >= 3):
                    pairs.append(tuple([s1.casefold(), s2.casefold()]))
    return len(pairs) >= 69