def all_substring_of_size_n(s):
    if len(s) < 24:
        return []
    result = set()
    for i in range(len(s) - 23):
        sub = s[i:i + 24]
        if len(set(sub)) == len(sub):
            result.add(sub)
    return list(result)