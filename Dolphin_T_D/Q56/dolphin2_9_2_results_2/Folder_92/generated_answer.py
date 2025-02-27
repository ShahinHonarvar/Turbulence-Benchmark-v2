def all_substring_of_size_n(s):
    if len(s) < 9:
        return []
    result = set()
    for i in range(len(s) - 8):
        sub = s[i:i + 9]
        if len(set(sub)) == 9:
            result.add(sub)
    return list(result)