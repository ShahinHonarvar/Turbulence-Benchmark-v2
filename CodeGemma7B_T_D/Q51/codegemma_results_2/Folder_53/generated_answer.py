def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        if not 3 <= len(string) <= 8:
            continue
        key = ''.join(sorted(string.lower()))
        if key not in anagrams:
            anagrams[key] = 1
        else:
            anagrams[key] += 1
            if anagrams[key] == 2:
                return True
    return False