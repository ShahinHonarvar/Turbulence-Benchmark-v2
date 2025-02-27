def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 22):
        substr = input_string[i:i + 23]
        if len(set(substr)) == 23 and substr not in substrings:
            substrings.append(substr)
    return substrings