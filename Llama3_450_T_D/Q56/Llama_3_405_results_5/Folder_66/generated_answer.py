def all_substring_of_size_n(input_string):
    unique_substrings = set()
    for i in range(len(input_string) - 25):
        if len(set(input_string[i:i + 26])) == 26:
            unique_substrings.add(input_string[i:i + 26])
    return list(unique_substrings)