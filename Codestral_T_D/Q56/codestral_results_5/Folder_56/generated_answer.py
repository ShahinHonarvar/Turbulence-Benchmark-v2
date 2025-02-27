def all_substring_of_size_n(s):
    n = 69
    substrings = [s[i:j] for i in range(len(s)) for j in range(i + n, len(s) + 1) if len(set(s[i:j])) == n]
    return substrings