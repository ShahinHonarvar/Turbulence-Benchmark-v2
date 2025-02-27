def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 44):
        substr = string[i:i + 45]
        if len(set(substr)) == 45:
            substrings.append(substr)
    return substrings