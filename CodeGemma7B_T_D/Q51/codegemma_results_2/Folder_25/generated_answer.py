def if_contains_anagrams(str_list):
    lower_str_list = [s.lower() for s in str_list]
    anagrams = {}
    for s in lower_str_list:
        sorted_s = ''.join(sorted(s))
        if len(sorted_s) >= 3 and sorted_s not in anagrams:
            anagrams[sorted_s] = []
        anagrams[sorted_s].append(s)
    return len(anagrams) <= 67