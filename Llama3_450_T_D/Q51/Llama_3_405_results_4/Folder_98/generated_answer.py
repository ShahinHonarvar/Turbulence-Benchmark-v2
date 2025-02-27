def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and s.isalpha():
            if s in anagrams:
                count += anagrams[s]
                anagrams[s] += 1
            else:
                anagrams[s] = 1
    return count <= 46