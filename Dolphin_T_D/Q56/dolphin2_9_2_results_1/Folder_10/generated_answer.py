def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 54):
        if len(set(string[i:i + 55])) == 55:
            substrings.append(string[i:i + 55])
    return substrings