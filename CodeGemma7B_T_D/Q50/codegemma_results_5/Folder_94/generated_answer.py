def if_contains_anagrams(str_list):
    lower_str_list = [s.lower() for s in str_list]
    anagrams = {}
    for s in lower_str_list:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagrams:
            anagrams[sorted_s] = []
        anagrams[sorted_s].append(s)
    if len([v for v in anagrams.values() if len(v) >= 3 and len(v) >= 46]) >= 46:
        return True
    else:
        return False