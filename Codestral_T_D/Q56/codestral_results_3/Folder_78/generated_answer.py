def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 49 + 1):
        substring = string[i:i + 49]
        if len(set(substring)) == 49:
            substrings.append(substring)
    return substrings