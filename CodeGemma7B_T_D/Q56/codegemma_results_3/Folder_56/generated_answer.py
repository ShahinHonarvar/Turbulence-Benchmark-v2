def all_substring_of_size_n(s):
    if len(s) < 69:
        return []
    return [s[i:i + 69] for i in range(len(s) - 68)]