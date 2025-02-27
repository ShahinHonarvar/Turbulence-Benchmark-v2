def all_substring_of_size_n(s):
    substrings = []
    length = len(s)
    if length < 34:
        return substrings
    for i in range(length - 33):
        substring = s[i:i + 34]
        if len(set(substring)) == 34:
            if substring not in substrings:
                substrings.append(substring)
    return substrings