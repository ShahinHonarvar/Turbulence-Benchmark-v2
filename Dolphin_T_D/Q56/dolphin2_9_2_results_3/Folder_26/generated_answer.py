def all_substring_of_size_n(s):
    n = len(s)
    return [s[i:i + 33] for i in range(n - 32) if len(set(s[i:i + 33])) == 33]