def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 54:
        return substrings
    for i in range(len(string) - 53):
        substring = string[i:i + 54]
        if len(set(substring)) == 54:
            substrings.append(substring)
    return substrings