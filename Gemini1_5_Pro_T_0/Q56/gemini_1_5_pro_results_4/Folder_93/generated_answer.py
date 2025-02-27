def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 54:
        return substrings
    for i in range(0, len(s) - 54 + 1):
        substring = s[i:i + 54]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings