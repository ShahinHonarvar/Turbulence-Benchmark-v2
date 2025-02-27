from collections import defaultdict

def if_contains_anagrams(str_list):
    """
    Checks if a list of strings contains at most 318 pairs of anagrams.
    """
    str_set = set()
    str_dict = defaultdict(list)
    for string in str_list:
        string_lower = string.lower()
        sorted_str = ''.join(sorted(string_lower))
        if sorted_str not in str_set:
            str_set.add(sorted_str)
            for key in str_dict:
                if len(str_dict[key]) >= 318:
                    return False
            str_dict[sorted_str].append(string)
        else:
            if len(str_dict[sorted_str]) >= 318:
                return False
            str_dict[sorted_str].append(string)
    return len(str_dict) <= 318