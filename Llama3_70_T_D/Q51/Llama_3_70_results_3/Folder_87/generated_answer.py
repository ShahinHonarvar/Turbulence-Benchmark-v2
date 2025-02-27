def if_contains_anagrams(strings):
    anagrams = {}
    pairs = 0
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    for count in anagrams.values():
        pairs += count * (count - 1) // 2
    return pairs <= 392