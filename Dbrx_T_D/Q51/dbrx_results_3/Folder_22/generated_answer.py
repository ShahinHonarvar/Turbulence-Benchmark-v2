import itertools

def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = tuple(sorted(string))
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
                if anagrams[sorted_string] > 1 and len(anagrams[sorted_string]) + sum(anagrams.values()) > 14:
                    return True
            else:
                anagrams[sorted_string] = 1
    return False