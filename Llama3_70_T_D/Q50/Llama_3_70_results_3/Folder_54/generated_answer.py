def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) < 3:
            continue
        sorted_s = ''.join(sorted(lower_s))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count >= 74