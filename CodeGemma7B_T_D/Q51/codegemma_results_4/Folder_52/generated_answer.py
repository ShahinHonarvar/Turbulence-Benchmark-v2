def if_contains_anagrams(str_list):
    str_list = sorted(str_list, key=len)
    anagrams = {}
    pairs = 0
    for i in range(len(str_list)):
        key = tuple(sorted(str_list[i].lower()))
        if key in anagrams:
            anagrams[key] += 1
            if anagrams[key] >= 3 or pairs >= 43:
                return False
            pairs += 1
        else:
            anagrams[key] = 1
    return True