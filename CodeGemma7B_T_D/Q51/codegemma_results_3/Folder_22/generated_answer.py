def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    anagrams = {}
    for s in str_list:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagrams:
            anagrams[sorted_s] = []
        anagrams[sorted_s].append(s)
    return len(anagrams) <= 14