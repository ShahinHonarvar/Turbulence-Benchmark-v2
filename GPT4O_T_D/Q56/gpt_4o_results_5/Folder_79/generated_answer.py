def all_substring_of_size_n(s):
    n = 61
    result = []
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            result.append(substr)
    return result