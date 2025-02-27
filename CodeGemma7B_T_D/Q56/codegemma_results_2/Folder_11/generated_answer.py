def all_substring_of_size_n(str):
    substrings = []
    for i in range(len(str)):
        for j in range(i + 78, len(str) + 1):
            substring = str[i:j]
            if len(substring) == 78 and (not substring in substrings):
                substrings.append(substring)
    return substrings