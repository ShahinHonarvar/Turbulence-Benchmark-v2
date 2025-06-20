def all_substring_of_size_n(s):
    substrings = []
    n = 81
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return substrings