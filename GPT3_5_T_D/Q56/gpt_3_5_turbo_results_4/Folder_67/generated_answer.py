def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 42):
        substring = string[i:i + 43]
        if len(set(substring)) == 43:
            substrings.append(substring)
    return substrings