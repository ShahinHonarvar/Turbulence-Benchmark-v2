def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        key = ''.join(sorted(word.lower()))
        if key in str_dict:
            if len(word) > 2:
                str_dict[key] += 1
        else:
            str_dict[key] = 1
    count = 0
    for value in str_dict.values():
        if value >= 411:
            count += 1
    return count >= 1