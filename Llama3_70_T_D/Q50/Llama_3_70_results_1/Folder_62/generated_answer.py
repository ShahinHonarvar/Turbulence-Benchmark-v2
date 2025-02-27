def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        lower = string.lower()
        sorted_str = ''.join(sorted(lower))
        if len(lower) < 3:
            continue
        if sorted_str in anagrams:
            anagrams[sorted_str].append(lower)
        else:
            anagrams[sorted_str] = [lower]
    pairs = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            pairs += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
        if pairs >= 43:
            return True
    return False