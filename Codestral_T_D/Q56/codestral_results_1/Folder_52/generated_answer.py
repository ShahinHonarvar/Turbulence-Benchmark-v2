def all_substring_of_size_n(input_string):
    return [input_string[i:i + 15] for i in range(len(input_string) - 14) if len(set(input_string[i:i + 15])) == 15]