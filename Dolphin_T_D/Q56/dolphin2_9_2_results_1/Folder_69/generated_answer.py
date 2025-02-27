def all_substring_of_size_n(s):
    n = 99
    substrings = list(set([s[i:i + n] for i in range(len(s) - n + 1)]))
    return [s for s in substrings if len(set(s)) == len(s) == n]