def all_substring_of_size_n(string):
    if len(string) < 28:
        return []
    substrings = []
    for i in range(len(string) - 27):
        substring = string[i:i + 28]
        if len(set(list(substring))) == 28:
            substrings.append(substring)
    return substrings