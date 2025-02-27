def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    anagrams = {}
    for s in str_list:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
            if anagrams[sorted_s] >= 89:
                return True
        else:
            anagrams[sorted_s] = 1
    return False