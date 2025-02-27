def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    l = [s[i:i + 43] for i in range(len(s) - 42)]
    return list(set(l))