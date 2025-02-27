def all_substring_of_size_n(input_string):
    if len(input_string) < 90:
        return []
    result = []
    for i in range(len(input_string) - 90):
        sub_string = input_string[i:i + 90]
        if len(set(sub_string)) == 90 and sub_string not in result:
            result.append(sub_string)
    return result