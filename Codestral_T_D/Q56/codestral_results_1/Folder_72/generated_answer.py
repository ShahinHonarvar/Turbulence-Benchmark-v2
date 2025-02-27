def all_substring_of_size_n(string):
    substrings = []
    length = len(string)
    for i in range(length - 87):
        substr = string[i:i + 88]
        if len(set(substr)) == 88:
            substrings.append(substr)
    return substrings