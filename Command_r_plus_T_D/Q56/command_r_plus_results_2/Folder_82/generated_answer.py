def all_substring_of_size_n(s):
    substrings = []
    length = len(s)
    for i in range(length):
        for j in range(i + 1, min(i + 101, length + 1)):
            substring = s[i:j]
            if len(substring) == 100 and len(substring) == len(set(substring)):
                substrings.append(substring)
    return substrings