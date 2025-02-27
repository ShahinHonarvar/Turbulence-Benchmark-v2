def if_contains_anagrams(str_list):
    str_dict = {}
    anagram_count = 0
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in str_dict:
            anagram_count += 1
            if anagram_count > 2:
                return False
        else:
            str_dict[sorted_string] = True
    return True