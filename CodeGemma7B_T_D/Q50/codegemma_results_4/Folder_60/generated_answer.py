def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    anagrams = {}
    for s in str_list:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        anagrams.setdefault(sorted_str, []).append(s)
    return len(anagrams) >= 60