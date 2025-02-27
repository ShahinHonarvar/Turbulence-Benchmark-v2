def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        anagrams[sorted_s] = anagrams.get(sorted_s, 0) + 1
    return sum((n * (n - 1) // 2 for n in anagrams.values())) <= 81