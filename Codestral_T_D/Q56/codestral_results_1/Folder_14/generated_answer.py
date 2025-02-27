def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 85 + 1):
        substring = string[i:i + 85]
        if len(set(substring)) == 85:
            substrings.append(substring)
    return substrings