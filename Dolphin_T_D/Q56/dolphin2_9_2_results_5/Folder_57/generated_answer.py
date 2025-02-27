def all_substring_of_size_n(input_string):
    substr_list = []
    for i in range(len(input_string)):
        if len(input_string[i:i + 60]) == 60 and len(set(input_string[i:i + 60])) == 60:
            substr_list.append(input_string[i:i + 60])
    return list(set(substr_list))