def if_contains_anagrams(strings):
    strings = [''.join(filter(str.isalpha, s)).lower() for s in strings if len(s) >= 3]
    anagrams = {}
    pairs = 0
    for s in strings:
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            pairs += len(anagrams[sorted_str])
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    return pairs <= 392