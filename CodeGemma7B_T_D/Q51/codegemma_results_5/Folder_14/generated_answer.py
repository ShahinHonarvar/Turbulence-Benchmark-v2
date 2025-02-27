def if_contains_anagrams(str_list):
    case_insensitive_str_list = [s.lower() for s in str_list]
    anagrams_dict = {}
    for string in case_insensitive_str_list:
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) >= 3 and sorted_string not in anagrams_dict:
            anagrams_dict[sorted_string] = string
    return len(anagrams_dict) <= 474