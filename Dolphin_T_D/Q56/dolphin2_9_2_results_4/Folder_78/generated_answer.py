def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    subs = [s[i:i + 49] for i in range(len(s) - 48)]
    return list(set(subs))