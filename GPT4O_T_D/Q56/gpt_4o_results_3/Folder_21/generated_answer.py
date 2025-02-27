def all_substring_of_size_n(s):
    result = []
    if len(s) < 106:
        return result
    for i in range(len(s) - 105):
        substr = s[i:i + 106]
        if len(set(substr)) == 106:
            result.append(substr)
    return result