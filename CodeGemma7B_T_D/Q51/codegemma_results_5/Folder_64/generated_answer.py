from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        if len(string) < 3:
            continue
        str_key = ''.join(sorted([c for c in string.lower() if c.isalpha()]))
        str_dict[str_key].append(string)
    for key, value in str_dict.items():
        if len(value) > 59:
            return False
    return True