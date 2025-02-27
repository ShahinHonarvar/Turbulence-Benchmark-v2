def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 130:
        return substrings
    for i in range(len(string) - 129):
        substring = string[i:i + 130]
        if len(set(substring)) == 130:
            substrings.append(substring)
    return substrings