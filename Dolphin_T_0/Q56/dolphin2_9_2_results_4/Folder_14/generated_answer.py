def all_substring_of_size_n(input_string):
    size = 85
    substrings = []
    for i in range(len(input_string) - size + 1):
        substr = input_string[i:i + size]
        if len(set(substr)) == size:
            substrings.append(substr)
    return substrings