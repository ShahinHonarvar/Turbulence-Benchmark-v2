def if_contains_anagrams(str_list):
    str_list = [''.join(sorted(i)) for i in str_list]
    new_dict = {}
    for string in str_list:
        if len(string) >= 3:
            if string not in new_dict:
                new_dict[string] = [string]
            else:
                n = len(new_dict[string])
                if n <= 92:
                    new_dict[string].append(string)
                elif n >= 93 and n + 1 <= len(str_list):
                    new_dict[string].append(string)
    return len(list(filter(lambda x: len(x) >= 93, new_dict.values()))) <= 1