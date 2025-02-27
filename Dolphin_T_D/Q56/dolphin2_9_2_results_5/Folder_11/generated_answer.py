def all_substring_of_size_n(s):
    if len(set(s)) == len(s):
        return [s[i:i + 78] for i in range(len(s) - 77)]
    return []