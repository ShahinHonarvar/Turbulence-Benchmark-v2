def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    n = len(s) // 63
    substrs = [s[i * 63:(i + 1) * 63] for i in range(n)]
    return substrs