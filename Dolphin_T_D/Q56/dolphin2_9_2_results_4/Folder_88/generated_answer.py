def all_substring_of_size_n(s):
    length = len(s)
    substrings = []
    if length < 68:
        return substrings
    for i in range(length - 67):
        substring = s[i:i + 68]
        if len(set(substring)) == 68:
            substrings.append(substring)
    return substrings