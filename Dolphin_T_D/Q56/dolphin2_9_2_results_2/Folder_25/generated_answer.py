def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 66):
        if len(set(input_string[i:i + 67])) == 67:
            substrings.append(input_string[i:i + 67])
    return substrings