def all_substring_of_size_n(s):
    if len(s) < 64:
        return []
    result = []
    for i in range(len(s) - 63):
        if len(set(s[i:i + 64])) == 64:
            result.append(s[i:i + 64])
    return result