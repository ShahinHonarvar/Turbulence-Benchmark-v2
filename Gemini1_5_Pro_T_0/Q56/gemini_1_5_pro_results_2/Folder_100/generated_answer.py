def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 92:
        return substrings
    for i in range(len(string) - 91):
        substring = string[i:i + 92]
        if len(set(substring)) == 92:
            if substring not in substrings:
                substrings.append(substring)
    return substrings