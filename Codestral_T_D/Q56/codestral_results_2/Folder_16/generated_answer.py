def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i + 124, len(string) + 1):
            substring = string[i:j]
            if len(set(substring)) == 124:
                substrings.append(substring)
    return substrings