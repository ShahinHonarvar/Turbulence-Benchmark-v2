def if_contains_anagrams(str_list):
    str_list = [item.lower() for item in str_list]
    str_dict = {}
    count = 0
    for string in str_list:
        sorted_string = ''.join(sorted(string))
        if sorted_string in str_dict:
            if len(string) >= 3 and len(str_dict[sorted_string]) >= 3:
                count += 1
            str_dict[sorted_string].append(string)
        else:
            str_dict[sorted_string] = [string]
    if count <= 48:
        return True
    else:
        return False