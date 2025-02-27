def all_substring_of_size_n(string):
    substrings = []
    length = len(string)
    for i in range(length - 89 + 1):
        substring = string[i:i + 89]
        if len(set(substring)) == 89:
            substrings.append(substring)
    return substrings