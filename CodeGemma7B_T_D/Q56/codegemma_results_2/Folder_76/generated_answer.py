def all_substring_of_size_n(input_string):
    list_size_n = []
    for i in range(len(input_string) - 148):
        list_size_n.append(input_string[i:i + 149])
    return list_size_n