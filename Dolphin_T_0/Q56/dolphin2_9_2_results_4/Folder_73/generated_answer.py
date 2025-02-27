def all_substring_of_size_n(s):
    n = len(s)
    if n < 20:
        return []
    substrings = []
    for i in range(n - 19):
        substring = s[i:i + 20]
        if set(substring).__len__() == len(substring):
            substrings.append(substring)
    return substrings