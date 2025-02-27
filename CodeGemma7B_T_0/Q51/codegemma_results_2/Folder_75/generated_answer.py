def if_contains_anagrams(str_list):
    anagrams = {}
    for s in str_list:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagrams.setdefault(key, []).append(s)
    return len(anagrams) <= 55