def all_substring_of_size_n(s):
    result = []
    n = len(s)
    if n < 57:
        return result
    for i in range(n - 56):
        substr = s[i:i + 57]
        if len(set(substr)) == 57:
            result.append(substr)
    return result