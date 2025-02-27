def all_substring_of_size_n(s):
    if len(set(s)) < 65:
        return []
    subs = [s[i:i + 65] for i in range(len(s) - 64)]
    return list(set(subs))