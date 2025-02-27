def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        sorted_s = ''.join(sorted(s_lower))
        if len(s_lower) >= 3 and s_lower.isalpha():
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pairs <= 55