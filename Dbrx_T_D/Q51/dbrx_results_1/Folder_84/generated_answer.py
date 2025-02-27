def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
                if anagrams[sorted_string] > 16:
                    return False
            else:
                anagrams[sorted_string] = 1
    return True