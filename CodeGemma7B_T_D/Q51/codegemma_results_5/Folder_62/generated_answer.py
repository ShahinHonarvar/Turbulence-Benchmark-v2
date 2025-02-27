def if_contains_anagrams(str_list):
    str_list = [word.lower() for word in str_list if len(word) >= 3]
    str_dict = {}
    for word in str_list:
        key = ''.join(sorted(word))
        str_dict.setdefault(key, []).append(word)
    return len(str_dict) <= 289