def all_substring_of_size_n(s):
    if len(s) < 3:
        return []
    substrings = []
    for i in range(len(s) - 2):
        if len(set(s[i:i + 3])) == 3:
            substrings.append(s[i:i + 3])
    return list(set(substrings))