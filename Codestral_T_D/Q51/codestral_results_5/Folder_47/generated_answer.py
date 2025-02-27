def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    pair_count = 0
    for count in anagrams.values():
        pair_count += count * (count - 1) // 2
    return pair_count <= 366