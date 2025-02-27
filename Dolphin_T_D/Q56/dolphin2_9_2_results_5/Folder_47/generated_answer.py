def all_substring_of_size_n(string):
    if len(string) < 91:
        return []
    substrings = []
    for i in range(len(string) - 80):
        substring = string[i:i + 91]
        if len(set(substring)) == 91:
            substrings.append(substring)
    return substrings