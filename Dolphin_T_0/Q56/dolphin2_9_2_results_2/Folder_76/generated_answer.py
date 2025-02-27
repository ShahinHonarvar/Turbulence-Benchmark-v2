def all_substring_of_size_n(s):
    n = len(s)
    substrings = []
    for i in range(n - 148):
        substring = s[i:i + 149]
        if len(set(substring)) == 149:
            substrings.append(substring)
    return substrings