def all_substring_of_size_n(input_string):
    result = []
    string_length = len(input_string)
    if string_length < 27:
        return result
    for i in range(string_length - 26):
        substring = input_string[i:i + 27]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result