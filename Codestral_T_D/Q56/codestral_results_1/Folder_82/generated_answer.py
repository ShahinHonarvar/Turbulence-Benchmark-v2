def all_substring_of_size_n(string):
    substrings = []
    length = len(string)
    if length < 100:
        return substrings
    for i in range(length - 100 + 1):
        substring = string[i:i + 100]
        if len(set(substring)) == 100:
            substrings.append(substring)
    return substrings