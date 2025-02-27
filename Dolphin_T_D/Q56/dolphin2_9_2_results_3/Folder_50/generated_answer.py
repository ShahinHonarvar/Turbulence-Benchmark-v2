def all_substring_of_size_n(s):
    if len(s) < 11:
        return []
    result = set()
    for i in range(len(s) - 11 + 1):
        if len(set(s[i:i + 11])) == 11:
            result.add(s[i:i + 11])
    return list(result)