def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    subs = [s[i:i + 14] for i in range(len(s) - 13)]
    subs = list(set(subs))
    return subs