def if_contains_anagrams(lst):
    anagrams = {}
    pairs = 0
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) < 3 or not s_lower.isalpha():
            continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagrams:
            pairs += anagrams[s_sorted]
            anagrams[s_sorted] += 1
        else:
            anagrams[s_sorted] = 1
    return pairs <= 84