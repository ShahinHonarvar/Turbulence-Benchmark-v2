def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_dict = {}
    for string in str_list:
        sorted_str = ''.join(sorted(string))
        if sorted_str not in str_dict:
            str_dict[sorted_str] = [string]
        else:
            str_dict[sorted_str].append(string)
    for anagram_list in str_dict.values():
        for i in range(len(anagram_list)):
            for j in range(i + 1, len(anagram_list)):
                if len(anagram_list[i]) >= 3 and len(anagram_list[j]) >= 3 and (anagram_list[i] != anagram_list[j]):
                    return True
    return False