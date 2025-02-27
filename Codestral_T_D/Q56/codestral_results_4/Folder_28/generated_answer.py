def all_substring_of_size_n(string):
    substrings = []
    length = len(string)
    if length < 44:
        return substrings
    for i in range(length - 43):
        substring = string[i:i + 44]
        if len(set(substring)) == 44:
            substrings.append(substring)
    return substrings