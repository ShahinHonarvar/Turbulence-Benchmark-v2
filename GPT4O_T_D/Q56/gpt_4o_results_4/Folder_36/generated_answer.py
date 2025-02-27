def all_substring_of_size_n(s):
    n = 146
    result = []
    length = len(s)
    if length < n:
        return result
    for i in range(length - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            result.append(substr)
    return result