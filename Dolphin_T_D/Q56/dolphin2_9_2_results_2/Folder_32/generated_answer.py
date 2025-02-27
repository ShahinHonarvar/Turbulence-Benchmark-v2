def all_substring_of_size_n(input_string):
    if len(set(input_string)) != len(input_string):
        return []
    else:
        return [input_string[i:i + 71] for i in range(len(input_string) - 71 + 1)]