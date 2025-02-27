def if_contains_anagrams(str_list):
    str_list_lower = [s.lower() for s in str_list]
    str_dict = {}
    for string in str_list_lower:
        sorted_string = ''.join(sorted(string))
        if sorted_string in str_dict:
            str_dict[sorted_string].append(string)
        else:
            str_dict[sorted_string] = [string]
    count = 0
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 3:
            count += len(anagram_list)
    if count >= 153:
        return True
    else:
        return False