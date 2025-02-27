def all_substring_of_size_n(s):
    result = []
    n = len(s)
    if n < 149:
        return result
    for i in range(n - 148):
        substr = s[i:i + 149]
        if len(set(substr)) == 149:
            result.append(substr)
    return result