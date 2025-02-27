def if_contains_anagrams(str_list):
    str_dict = {}
    for str in str_list:
        str = str.lower()
        sorted_str = ''.join(sorted(str))
        if sorted_str not in str_dict:
            str_dict[sorted_str] = []
        str_dict[sorted_str].append(str)
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 17:
            return True
    return False