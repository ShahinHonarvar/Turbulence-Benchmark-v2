def all_substring_of_size_n(string):
    str_list = []
    for i in range(len(string)):
        for j in range(i + 63, len(string) + 1):
            str_list.append(string[i:j])
    return list(set(str_list))