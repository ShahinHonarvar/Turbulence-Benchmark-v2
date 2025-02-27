def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    res = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                res += 1
    return res >= 58