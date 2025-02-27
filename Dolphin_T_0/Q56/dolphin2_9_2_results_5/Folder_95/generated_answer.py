def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    return [s[i:i + 89] for i in range(len(s) - 89)]