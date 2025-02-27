from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted((word.lower() for word in string if len(word) >= 3)))
        str_dict[sorted_str].append(string)
    return len(list(filter(lambda x: len(x) >= 136, str_dict.values()))) >= 1