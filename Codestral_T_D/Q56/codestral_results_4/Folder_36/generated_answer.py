def all_substring_of_size_n(string):
    substrings = []
    length = len(string)
    for i in range(length):
        for j in range(i + 146, length + 1):
            substring = string[i:j]
            if len(set(substring)) == 146:
                substrings.append(substring)
    return substrings