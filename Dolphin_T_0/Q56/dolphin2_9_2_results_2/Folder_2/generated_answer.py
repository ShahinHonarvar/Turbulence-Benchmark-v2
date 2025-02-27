def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 55):
        if len(set(input_string[i:i + 56])) == 56:
            substrings.append(input_string[i:i + 56])
    return substrings if substrings else []