def if_contains_anagrams(strings):
    n = len(strings)
    anagrams = 0
    for i in range(n):
        for j in range(i + 1, n):
            if len(strings[i]) < 3 or len(strings[j]) < 3:
                continue
            s1 = ''.join(sorted(strings[i].lower()))
            s2 = ''.join(sorted(strings[j].lower()))
            if s1 == s2:
                anagrams += 1
    return anagrams <= 24