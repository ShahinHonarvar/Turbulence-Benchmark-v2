def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams.values() if n > 1))
    return pairs <= 38