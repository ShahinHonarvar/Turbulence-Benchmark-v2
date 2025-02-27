def if_contains_anagrams(lst):
    anagrams_count = {}
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        key = ''.join(sorted(s))
        anagrams_count[key] = anagrams_count.get(key, 0) + 1
    count = 0
    for v in anagrams_count.values():
        count += v * (v - 1) // 2
    return count <= 43