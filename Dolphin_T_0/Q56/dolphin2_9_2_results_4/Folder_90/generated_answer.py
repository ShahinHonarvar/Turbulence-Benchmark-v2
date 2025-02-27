def all_substring_of_size_n(s):
    length = 130
    substrings = []
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            substrings.append(substring)
    return list(set(substrings))