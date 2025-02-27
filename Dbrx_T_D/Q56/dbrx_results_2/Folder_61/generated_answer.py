def all_substring_of_size_n(s):
    if len(s) < 39 or len(set(s)) != len(s):
        return []
    else:
        return [s[i:i + 39] for i in range(len(s) - 38)]