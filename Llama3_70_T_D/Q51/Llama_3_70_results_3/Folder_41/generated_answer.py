def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s = s.lower()
        sorted_s = ''.join(sorted(s))
        if len(s) < 3 or not s.isalpha():
            continue
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    pairs = 0
    for k in anagrams:
        l = len(anagrams[k])
        pairs += l * (l - 1) // 2
    return pairs <= 52