def all_substring_of_size_n(string):
    length = len(string)
    substrings = []
    if length < 65:
        return substrings
    for i in range(length - 64):
        substring = string[i:i + 65]
        if len(set(substring)) == 65:
            substrings.append(substring)
    return substrings