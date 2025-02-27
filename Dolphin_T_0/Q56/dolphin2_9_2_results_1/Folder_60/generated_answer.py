def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    substrings = [s[i:i + 36] for i in range(len(s) - 35)]
    return substrings