def if_contains_anagrams(str_list):
    anagrams = {}
    for s in str_list:
        s = ''.join(sorted(s.lower()))
        if len(s) < 3:
            continue
        if s in anagrams:
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    if len(anagrams) <= 39:
        return True
    return False