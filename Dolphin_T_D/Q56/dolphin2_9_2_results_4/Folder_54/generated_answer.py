def all_substring_of_size_n(s):
    if len(s) < 28:
        return []
    result = []
    for i in range(len(s) - 27):
        substr = s[i:i + 28]
        if len(set(substr)) == 28:
            result.append(substr)
    return result