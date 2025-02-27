def all_substring_of_size_n(s):
    if len(s) < 106:
        return []
    result = []
    for i in range(len(s) - 105):
        if len(set(s[i:i + 106])) == 106:
            result.append(s[i:i + 106])
    return result