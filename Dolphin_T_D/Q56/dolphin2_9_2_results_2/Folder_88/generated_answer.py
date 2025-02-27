def all_substring_of_size_n(s):
    if len(s) < 68:
        return []
    n = len(set(s))
    if n < 68:
        return []
    res = [s[i:i + 68] for i in range(len(s) - 67)]
    return [x for x in set(res)]