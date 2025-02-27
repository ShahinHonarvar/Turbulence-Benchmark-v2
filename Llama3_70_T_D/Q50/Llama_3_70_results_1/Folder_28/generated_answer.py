def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and sorted_s in anagrams:
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count >= 81