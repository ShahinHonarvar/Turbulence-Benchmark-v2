def all_substring_of_size_n(s):
    result = []
    if len(s) < 74:
        return result
    n = len(s)
    for i in range(n - 73):
        if len(set(s[i:i + 74])) == 74:
            result.append(s[i:i + 74])
    return result