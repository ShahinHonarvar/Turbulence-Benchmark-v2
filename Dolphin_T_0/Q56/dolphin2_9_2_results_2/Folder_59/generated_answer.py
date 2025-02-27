def all_substring_of_size_n(input_string):
    result = []
    for i in range(len(input_string) - 76):
        sub_string = input_string[i:i + 77]
        if sub_string == ''.join(sorted(sub_string)) and sub_string not in result:
            result.append(sub_string)
    return result