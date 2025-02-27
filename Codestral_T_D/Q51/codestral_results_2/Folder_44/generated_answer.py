def if_contains_anagrams(strings):
    count = 0
    anagrams = {}
    for string in strings:
        s = ''.join(sorted(string.lower()))
        if len(s) >= 3:
            if s not in anagrams:
                anagrams[s] = 0
            anagrams[s] += 1
            count += anagrams[s] - 1
    return count <= 75