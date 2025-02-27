def if_contains_anagrams(str_list):
    anagrams = {}
    for s in str_list:
        s = s.lower()
        key = ''.join(sorted(s))
        anagrams[key] = anagrams.get(key, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pairs <= 72