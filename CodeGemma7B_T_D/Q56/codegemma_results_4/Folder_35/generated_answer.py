def all_substring_of_size_n(str):
    list = []
    i = 0
    j = 27
    while j <= len(str):
        sub_str = str[i:j]
        i += 1
        j += 1
        if len(set(sub_str)) == 27:
            list.append(sub_str)
    return list