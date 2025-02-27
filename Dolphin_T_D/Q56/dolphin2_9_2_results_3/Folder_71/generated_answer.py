def all_substring_of_size_n(input_string):
    substr_list = []
    for i in range(len(input_string) - 17 + 1):
        substr = input_string[i:i + 17]
        if len(set(substr)) == 17:
            substr_list.append(substr)
    return list(set(substr_list))