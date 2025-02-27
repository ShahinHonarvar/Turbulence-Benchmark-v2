def all_substring_of_size_n(s):
    if len(s) < 12:
        return []
    result = set()
    for i in range(len(s) - 12 + 1):
        sub = s[i:i + 12]
        if len(set(sub)) == 12:
            result.add(sub)
    return list(result)