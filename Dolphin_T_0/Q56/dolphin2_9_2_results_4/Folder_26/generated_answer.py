def all_substring_of_size_n(s):
    if len(set(s)) < 33:
        return []
    return [s[i:i + 33] for i in range(len(s) - 33 + 1) if len(set(s[i:i + 33])) == 33]