def all_substrings_of_size_n(s):
    if len(set(s)) < 29:
        return []
    result = set()
    for i in range(len(s) - 28):
        sub = s[i:i + 29]
        if len(set(sub)) == 29:
            result.add(sub)
    return list(result)