def all_substring_of_size_n(input_string):
    return_list = []
    if len(input_string) < 91:
        return return_list
    for i in range(len(input_string) - 91):
        sub_string = input_string[i:i + 92]
        if len(set(sub_string)) == len(sub_string):
            return_list.append(sub_string)
    return return_list