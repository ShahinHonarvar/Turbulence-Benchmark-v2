def all_substring_of_size_n(s):
    if len(s) < 44:
        return []
    return list(set([s[i:i + 44] for i in range(len(s) - 43)]))