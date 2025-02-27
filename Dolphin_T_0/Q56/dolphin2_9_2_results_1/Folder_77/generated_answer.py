def all_substring_of_size_n(s):
    n = 144
    substrings = []
    for i in range(len(s) - n + 1):
        if len(set(s[i:i + n])) == n:
            substrings.append(s[i:i + n])
    return list(set(substrings))