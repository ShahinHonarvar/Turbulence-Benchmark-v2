def if_contains_anagrams(lst):
    anagrams = {}
    pairs = 0
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            pairs += anagrams[sorted_s]
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    return pairs <= 68