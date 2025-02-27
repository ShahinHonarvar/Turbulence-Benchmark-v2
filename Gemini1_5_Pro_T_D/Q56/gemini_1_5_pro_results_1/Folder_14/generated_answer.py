def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 85:
        return substrings
    for i in range(len(string) - 84):
        substring = string[i:i + 85]
        if len(set(substring)) == 85:
            if substring not in substrings:
                substrings.append(substring)
    return substrings