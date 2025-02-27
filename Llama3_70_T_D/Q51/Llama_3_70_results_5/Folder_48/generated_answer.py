def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        if len(s) < 3:
            continue
        s = ''.join(filter(str.isalpha, s)).lower()
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    for v in anagrams.values():
        n = len(v)
        count += n * (n - 1) // 2
    return count <= 277