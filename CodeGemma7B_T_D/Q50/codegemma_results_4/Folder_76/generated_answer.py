def if_contains_anagrams(str_list):
    str_map = {}
    for str in str_list:
        str = str.lower()
        sorted_str = ''.join(sorted(str))
        if sorted_str not in str_map:
            str_map[sorted_str] = []
        str_map[sorted_str].append(str)
    for anagram_list in str_map.values():
        if len(anagram_list) >= 143 and all((len(s) >= 3 for s in anagram_list)):
            return True
    return False