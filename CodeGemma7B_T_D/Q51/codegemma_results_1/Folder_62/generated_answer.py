def if_contains_anagrams(str_list):
    str_list.sort()
    str_dict = {}
    for string in str_list:
        key = ''.join(sorted([char for char in string.lower() if char.isalpha()]))
        str_dict[key] = str_dict.get(key, []) + [string]
    return len(str_dict) <= 289