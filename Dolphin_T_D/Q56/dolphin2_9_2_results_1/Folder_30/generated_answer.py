def all_substring_of_size_n(input_string):
    if len(set(input_string)) != len(input_string) or len(input_string) < 79:
        return []
    return [input_string[i:i + 79] for i in range(len(input_string) - 78)]