def all_substring_of_size_n(s):
    if len(set(s)) != 23:
        return []
    subs = [s[i:i + 23] for i in range(len(s) - 22)]
    return list(set(subs))