def all_substring_of_size_n(s):
    if len(s) < 12:
        return []
    substrings = []
    for i in range(len(s) - 12 + 1):
        substring = s[i:i + 12]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings