def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagrams:
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    count = 0
    for value in anagrams.values():
        count += value * (value - 1) // 2
        if count > 72:
            return False
    return True