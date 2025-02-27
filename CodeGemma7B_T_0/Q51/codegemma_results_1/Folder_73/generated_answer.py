def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and sorted_string not in anagrams:
            anagrams[sorted_string] = string
    return len(anagrams) <= 279