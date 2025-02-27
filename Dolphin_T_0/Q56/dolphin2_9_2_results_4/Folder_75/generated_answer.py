def all_substring_of_size_n(input_string):
    if len(input_string) < 16:
        return []
    substring_list = []
    for i in range(len(input_string) - 15):
        if len(set(input_string[i:i + 16])) == 16:
            substring_list.append(input_string[i:i + 16])
    return list(set(substring_list))