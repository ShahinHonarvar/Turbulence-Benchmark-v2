def all_substring_of_size_n(s):
    n = 74
    result = []
    length = len(s)
    for i in range(length - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            result.append(substr)
    return result