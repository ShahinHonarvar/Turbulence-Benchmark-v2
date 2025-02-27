def all_substrings_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    n = len(s)
    return [s[i:i + 70] for i in range(n - 69)]