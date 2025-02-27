def if_contains_anagrams(str_list):
    anagrams = set()
    for s in str_list:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams.add(s)
    return len(anagrams) <= 92