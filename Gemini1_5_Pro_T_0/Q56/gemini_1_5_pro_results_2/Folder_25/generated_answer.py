def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 67:
        return substrings
    for i in range(len(string) - 66):
        substring = string[i:i + 67]
        if len(set(substring)) == 67:
            if substring not in substrings:
                substrings.append(substring)
    return substrings