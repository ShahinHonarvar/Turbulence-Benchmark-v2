from collections import defaultdict

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_dict = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string))
        str_dict[sorted_string].append(string)
    return len([anagrams for anagrams in str_dict.values() if len(anagrams) > 3]) <= 4