def all_substring_of_size_n(s):
    if len(s) < 39:
        return []
    result = []
    for i in range(len(s) - 38):
        substr = s[i:i + 39]
        if len(set(substr)) == 39:
            result.append(substr)
    return list(set(result))