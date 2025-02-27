def all_substring_of_size_n(s):
    if len(s) < 6:
        return []
    n = len((set(s[i:i + 6]) >= 6 for i in range(len(s) - 5)))
    return [s[i:i + 6] for i in range(len(s) - 5) if len(set(s[i:i + 6])) == 6]