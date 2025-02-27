def all_substring_of_size_n(s):
    if len(set(s)) != 84:
        return []
    return [s[i:i + 84] for i in range(len(s) - 84 + 1)]