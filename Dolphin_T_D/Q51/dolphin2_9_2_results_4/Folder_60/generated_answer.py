def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) < 3 or not word.isalpha():
            continue
        k = ''.join(sorted(word.lower()))
        if k in anagrams:
            anagrams[k] += 1
        else:
            anagrams[k] = 1
    pairs = 0
    for v in anagrams.values():
        if v > 1:
            pairs += v * (v - 1) // 2
    return pairs <= 77