def if_contains_anagrams(str_list):
    str_dict = {}
    for str in str_list:
        str = str.lower()
        sorted_str = ''.join(sorted(str))
        if len(sorted_str) >= 3:
            if str_dict.get(sorted_str) is None:
                str_dict[sorted_str] = [str]
            else:
                str_dict[sorted_str].append(str)
    anagram_num = 0
    for str_list in str_dict.values():
        anagram_num += int(len(str_list) * (len(str_list) - 1) / 2)
    if anagram_num >= 153:
        return True
    else:
        return False