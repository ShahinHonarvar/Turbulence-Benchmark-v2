def if_contains_anagrams(str_list):
    str_list = sorted(str_list, key=len)
    char_dict = {}
    count = 0
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str not in char_dict:
            if len(sorted_str) >= 3:
                char_dict[sorted_str] = [string]
        else:
            if len(sorted_str) >= 3:
                if len(char_dict[sorted_str]) >= 79:
                    count += 1
            char_dict[sorted_str].append(string)
    return count >= 79