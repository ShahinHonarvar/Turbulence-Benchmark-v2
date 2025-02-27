def if_contains_anagrams(str_list):
    anagrams = {}
    for s in str_list:
        key = ''.join(sorted(s.lower()))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    return sum((v for v in anagrams.values() if v > 1)) <= 70