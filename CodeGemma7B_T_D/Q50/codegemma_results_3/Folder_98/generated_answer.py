from collections import Counter

def if_contains_anagrams(str_list):
    str_list_upper = [s.upper() for s in str_list]
    str_list_filtered = [s for s in str_list_upper if len(s) >= 3]
    anagrams_dict = {}
    for string in str_list_filtered:
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagrams_dict:
            anagrams_dict[sorted_string] = [string]
        else:
            anagrams_dict[sorted_string] += [string]
    return len(anagrams_dict) >= 7