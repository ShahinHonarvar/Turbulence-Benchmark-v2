def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 29:
        return substrings
    for i in range(len(string) - 29 + 1):
        substring = string[i:i + 29]
        if len(set(substring)) == 29 and substring not in substrings:
            substrings.append(substring)
    return substrings