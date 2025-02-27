def if_contains_anagrams(str_list):
    anagrams = {}
    for s in str_list:
        key = ''.join(sorted(s.lower()))
        if key not in anagrams or len(anagrams[key]) < 3:
            anagrams[key] = s
    return len({v for v in anagrams.values()}) <= 17