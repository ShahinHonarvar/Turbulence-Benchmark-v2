def all_substring_of_size_n(s):
    if len(set(s)) != len(s) or len(s) < 78:
        return []
    return [s[i:i + 78] for i in range(len(s) - 77)]