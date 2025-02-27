def all_substring_of_size_n(str):
    length = len(str)
    list = []
    for i in range(length):
        for j in range(i + 1, min(i + 98 + 1, length + 1)):
            sub_string = str[i:j]
            if len(set(sub_string)) == 98:
                list.append(sub_string)
    return list