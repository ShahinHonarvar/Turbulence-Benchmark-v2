def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        if not string or len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    return len(anagrams) <= 401