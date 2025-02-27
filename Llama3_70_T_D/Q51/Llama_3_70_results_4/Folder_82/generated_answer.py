def if_contains_anagrams(strings):
    strings = [''.join(filter(str.isalpha, s)).lower() for s in strings if len(''.join(filter(str.isalpha, s))) >= 3]
    anagrams = {}
    for s in strings:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return pairs <= 40