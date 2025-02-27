def all_substring_of_size_n(string):
    n = 65
    substrings = []
    for i in range(len(string)):
        for j in range(i + n, len(string) + 1):
            substring = string[i:j]
            if len(substring) == len(set(substring)):
                substrings.append(substring)
    return substrings