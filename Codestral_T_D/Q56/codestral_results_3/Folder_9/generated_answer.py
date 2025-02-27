def all_substring_of_size_n(string):
    if len(string) < 34:
        return []
    substrings = []
    for i in range(len(string) - 33):
        substring = string[i:i + 34]
        if len(set(substring)) == 34:
            substrings.append(substring)
    return substrings