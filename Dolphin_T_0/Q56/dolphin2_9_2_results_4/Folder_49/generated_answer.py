def all_substring_of_size_n(s):
    n = len(s)
    substrings = []
    for i in range(n):
        if len(set(s[i:i + 73])) == 73:
            substrings.append(s[i:i + 73])
    return list(set(substrings))