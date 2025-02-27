def if_contains_anagrams(str_list):
    str_dict = {}
    count = 0
    for string in str_list:
        letters = sorted(string.lower())
        key = ''.join(letters)
        if key in str_dict:
            count += 1
        else:
            str_dict[key] = string
    return count <= 35