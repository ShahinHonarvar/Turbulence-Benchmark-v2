def all_substring_of_size_n(input_string):
    result = []
    string_length = len(input_string)
    for i in range(0, string_length - 84):
        substring = input_string[i:i + 85]
        if len(set(substring)) == 85:
            result.append(substring)
    return result