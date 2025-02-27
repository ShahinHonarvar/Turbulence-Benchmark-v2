def all_substring_of_size_n(input_string):
    if len(input_string) != 44:
        return []
    return [input_string[i:i + 44] for i in range(0, len(input_string) - 43) if len(set(input_string[i:i + 44])) == 44]