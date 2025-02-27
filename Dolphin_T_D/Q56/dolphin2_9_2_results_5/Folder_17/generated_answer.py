def all_substring_of_size_n(s):
    if len(set(s)) < 37:
        return []
    result = []
    for i in range(len(s) - 36):
        if len(set(s[i:i + 37])) == 37:
            result.append(s[i:i + 37])
    return result