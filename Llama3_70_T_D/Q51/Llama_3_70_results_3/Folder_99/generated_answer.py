def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        s = ''.join(filter(str.isalpha, s))
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    count = sum((len(value) * (len(value) - 1) // 2 for value in anagrams.values()))
    return count <= 93