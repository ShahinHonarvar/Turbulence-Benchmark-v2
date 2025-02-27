def all_substring_of_size_n(s):
    if len(s) < 20:
        return []
    substrings = []
    for i in range(len(s) - 19):
        substring = s[i:i + 20]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return list(set(substrings))