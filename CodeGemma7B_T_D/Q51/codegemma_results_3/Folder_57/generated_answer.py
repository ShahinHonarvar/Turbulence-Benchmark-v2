from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(int)
    for string in str_list:
        sorted_str = ''.join(sorted([c for c in string.lower() if c.isalpha() and len(c) >= 3]))
        str_dict[sorted_str] += 1
    return len(str_dict) <= 74