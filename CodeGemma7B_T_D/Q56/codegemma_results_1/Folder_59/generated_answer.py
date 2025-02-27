def all_substring_of_size_n(str):
    substring_list = []
    for i in range(len(str) - 76):
        substring_list.append(str[i:i + 77])
    return list(set(substring_list))