def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        s = ''.join(sorted(s.lower()))
        if s in anagrams:
            count += anagrams[s]
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    return count <= 61