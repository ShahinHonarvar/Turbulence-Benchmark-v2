def all_substring_of_size_n(s):
    if len(s) < 92 or len(set(s)) != 92:
        return []
    return [s[i:i + 92] for i in range(len(s) - 92 + 1)]