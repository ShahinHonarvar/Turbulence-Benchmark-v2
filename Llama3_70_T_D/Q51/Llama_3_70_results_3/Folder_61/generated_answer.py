def if_contains_anagrams(lst):
    anagrams_count = {}
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams_count:
            anagrams_count[sorted_s] += 1
        else:
            anagrams_count[sorted_s] = 1
    pairs_count = sum(((count - 1) * count // 2 for count in anagrams_count.values()))
    return pairs_count <= 50