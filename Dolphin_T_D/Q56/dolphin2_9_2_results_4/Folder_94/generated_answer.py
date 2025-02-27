def all_substring_of_size_n(s):
    if len(set(s)) < 70:
        return []
    return [s[i:i + 70] for i in range(0, len(s) - 70 + 1) if len(set(s[i:i + 70])) == 70]