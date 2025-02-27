def all_substring_of_size_n(string):
    substrings = []
    length = len(string)
    if length < 127:
        return substrings
    for i in range(length - 126):
        substring = string[i:i + 127]
        if len(set(substring)) == 127:
            substrings.append(substring)
    return substrings