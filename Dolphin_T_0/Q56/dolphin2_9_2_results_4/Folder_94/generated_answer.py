def all_substring_of_size_n(input_string):
    result = []
    for i in range(len(input_string) - 69):
        sub_string = input_string[i:i + 70]
        if len(sub_string) == len(set(sub_string)):
            result.append(sub_string)
    return result