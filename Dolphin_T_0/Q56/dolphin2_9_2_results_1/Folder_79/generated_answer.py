def all_substring_of_size_n(s):
    n = len(s)
    substrings = []
    for i in range(n - 60):
        substring = s[i:i + 61]
        if len(set(substring)) == 61:
            substrings.append(substring)
    return list(set(substrings))