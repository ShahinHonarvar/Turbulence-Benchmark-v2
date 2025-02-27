def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = sorted(str_list, key=len)
    anagrams = {}
    for s in str_list:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 0
    for key, value in anagrams.items():
        if len(key) >= 3 and value >= 5:
            return True
    return False