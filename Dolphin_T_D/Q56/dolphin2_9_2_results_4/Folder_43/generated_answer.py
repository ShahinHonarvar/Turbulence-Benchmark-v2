def all_substring_of_size_n(s):
    n = 86
    if len(set(s)) != n:
        return []
    res = [s[i:i + n] for i in range(len(s) - n + 1)]
    return res if len(set(res)) == len(res) else []