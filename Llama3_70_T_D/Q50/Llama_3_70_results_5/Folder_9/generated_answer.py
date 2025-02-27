def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        s = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if s in anagrams:
                anagrams[s] += 1
            else:
                anagrams[s] = 1
    for key in anagrams:
        count += anagrams[key] * (anagrams[key] - 1) // 2
    return count >= 66