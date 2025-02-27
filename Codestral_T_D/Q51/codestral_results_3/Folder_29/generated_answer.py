def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagrams:
            anagrams[sorted_s] = 0
        anagrams[sorted_s] += 1
    count = 0
    for val in anagrams.values():
        count += val * (val - 1) // 2
    return count <= 318