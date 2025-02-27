def all_substring_of_size_n(string):
    if len(string) < 110:
        return []
    substrings = []
    for i in range(len(string) - 110):
        substring = string[i:i + 110]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings