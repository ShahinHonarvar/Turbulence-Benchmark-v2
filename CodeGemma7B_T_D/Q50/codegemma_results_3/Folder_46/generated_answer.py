from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [s for s in str_list if len(s) >= 3]
    str_dict = {Counter(s): s for s in str_list}
    return len(str_dict) >= 38