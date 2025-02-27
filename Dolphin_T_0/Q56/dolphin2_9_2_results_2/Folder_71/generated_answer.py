def all_substring_of_size_n(string):
    if len(string) < 17:
        return []
    substrings = []
    for i in range(len(string) - 17 + 1):
        substring = string[i:i + 17]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings