def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        s = ''.join(sorted(s))
        if s in anagrams:
            count += anagrams[s]
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    return count <= 15