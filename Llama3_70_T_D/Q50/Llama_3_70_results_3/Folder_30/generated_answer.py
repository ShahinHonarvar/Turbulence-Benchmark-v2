def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        if len(string) >= 3:
            s = ''.join(sorted(string.lower()))
            if s in anagrams:
                anagrams[s] += 1
            else:
                anagrams[s] = 1
    for v in anagrams.values():
        count += v * (v - 1) // 2
    return count >= 78