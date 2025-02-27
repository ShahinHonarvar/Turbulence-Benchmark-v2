def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    count = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if sorted(strings[i]) == sorted(strings[j]):
                count += 1
    return count >= 96