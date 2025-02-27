def all_substring_of_size_n(s):
    substrings = []
    n = len(s)
    for i in range(n - 46):
        substring = s[i:i + 47]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings