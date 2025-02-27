def if_contains_anagrams(str_list):
    anagrams = {}
    for s in str_list:
        s = ''.join(sorted(s.lower()))
        if len(s) < 3:
            continue
        if s not in anagrams:
            anagrams[s] = []
        anagrams[s].append(s)
    return len(anagrams) <= 401