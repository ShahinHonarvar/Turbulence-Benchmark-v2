def all_substring_of_size_n(string):
    substrings = []
    length = len(string)
    for i in range(length - 59):
        substring = string[i:i + 60]
        if len(set(substring)) == 60:
            substrings.append(substring)
    return substrings