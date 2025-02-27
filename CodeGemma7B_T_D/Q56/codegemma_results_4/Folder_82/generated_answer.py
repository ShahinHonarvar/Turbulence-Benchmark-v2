def all_substring_of_size_n(string):
    if len(string) < 100:
        return []
    substrings = []
    for i in range(len(string) - 100 + 1):
        substring = string[i:i + 100]
        if not substring in substrings:
            substrings.append(substring)
    return substrings