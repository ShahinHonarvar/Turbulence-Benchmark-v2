def all_substring_of_size_n(s):
    length = len(s)
    substrings = []
    for i in range(length):
        for j in range(i + 63, length):
            substring = s[i:j]
            if len(set(substring)) == len(substring) == 63:
                substrings.append(substring)
    return substrings