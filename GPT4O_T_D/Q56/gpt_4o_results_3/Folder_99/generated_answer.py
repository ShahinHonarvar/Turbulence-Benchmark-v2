def all_substring_of_size_n(s):
    n = len(s)
    if n < 110:
        return []
    result = []
    for i in range(n - 109):
        substring = s[i:i + 110]
        if len(set(substring)) == 110:
            result.append(substring)
    return result