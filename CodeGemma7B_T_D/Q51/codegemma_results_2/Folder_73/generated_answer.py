def if_contains_anagrams(str_list):
    anagrams = {}
    for str in str_list:
        str = ''.join(sorted(str.lower()))
        if len(str) >= 3 and str in anagrams:
            anagrams[str] += 1
            if anagrams[str] > 279:
                return False
        else:
            anagrams[str] = 1
    return True