def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if len(string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    return len(anagrams) >= 312