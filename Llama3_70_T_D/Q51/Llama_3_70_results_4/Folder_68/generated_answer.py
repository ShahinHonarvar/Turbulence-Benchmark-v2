def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        s = s.lower()
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    count_pairs = sum((v * (v - 1) // 2 for v in anagrams.values() if v > 1))
    return count_pairs <= 94