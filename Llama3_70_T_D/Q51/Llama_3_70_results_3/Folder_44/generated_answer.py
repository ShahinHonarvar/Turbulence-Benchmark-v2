def if_contains_anagrams(strs):
    anagrams_count = {}
    for s in strs:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        s = ''.join(sorted(s))
        anagrams_count[s] = anagrams_count.get(s, 0) + 1
    pairs = sum((x * (x - 1) // 2 for x in anagrams_count.values()))
    return pairs <= 75