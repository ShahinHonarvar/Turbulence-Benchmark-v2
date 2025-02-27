def all_substring_of_size_n(s):
    length = len(s)
    substrings = []
    for i in range(length):
        for j in range(i + 6, length + 1):
            substring = s[i:j]
            if len(set(substring)) == len(substring) == 6:
                substrings.append(substring)
    return substrings