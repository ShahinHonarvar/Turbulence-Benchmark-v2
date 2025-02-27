def all_substring_of_size_n(s):
    if len(s) != 42:
        return []
    n = len(s)
    substrings = []
    for i in range(n - 41):
        substring = s[i:i + 42]
        if len(set(substring)) == 42:
            substrings.append(substring)
    return substrings