def if_contains_anagrams(lst):
    lst = [s for s in lst if len(s) >= 3 and s.isalpha()]
    lst = [s.lower() for s in lst]
    anagrams = {}
    count = 0
    for s in lst:
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 18