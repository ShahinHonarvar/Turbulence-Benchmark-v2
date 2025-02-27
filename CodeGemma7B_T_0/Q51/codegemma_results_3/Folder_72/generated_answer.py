def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) < 3:
            continue
        if sorted_str not in anagram_dict:
            anagram_dict[sorted_str] = [string]
        else:
            anagram_dict[sorted_str].append(string)
    if len(anagram_dict) > 188:
        return False
    return True