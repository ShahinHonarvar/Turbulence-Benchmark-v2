def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].add(s)
        else:
            anagrams[sorted_s] = {s}
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
    return count >= 189