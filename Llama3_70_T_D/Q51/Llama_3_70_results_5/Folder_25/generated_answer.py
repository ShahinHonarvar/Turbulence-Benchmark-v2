def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        if len(s) < 3:
            continue
        s = ''.join(filter(str.isalpha, s)).lower()
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    for v in anagrams.values():
        count += v * (v - 1) // 2
    return count <= 67