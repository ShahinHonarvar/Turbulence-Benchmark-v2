def all_substring_of_size_n(s):
    if len(set(s)) < 57:
        return []
    return [s[i:i + 57] for i in range(len(s) - 56)]