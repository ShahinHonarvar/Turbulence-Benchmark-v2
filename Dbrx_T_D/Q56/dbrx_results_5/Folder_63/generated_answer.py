def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 19:
        return []
    for i in range(len(s) - 18):
        substring = s[i:i + 19]
        if len(set(substring)) == 19:
            substrings.append(substring)
    return list(set(substrings))