def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        string = sorted(string.lower())
        if len(string) < 3:
            continue
        key = ''.join(string)
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    return len(anagrams) <= 68