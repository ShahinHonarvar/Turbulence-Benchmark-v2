def all_substring_of_size_n(s):
    if len(s) < 23:
        return []
    return [s[i:i + 23] for i in range(len(s) - 22) if len(set(s[i:i + 23])) == 23]