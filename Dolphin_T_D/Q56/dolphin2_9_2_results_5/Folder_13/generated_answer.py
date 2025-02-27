def all_substring_of_size_n(input_string):
    result = []
    for i in range(len(input_string) - 52):
        sub_string = input_string[i:i + 53]
        if len(set(sub_string)) == len(sub_string):
            result.append(sub_string)
    return result