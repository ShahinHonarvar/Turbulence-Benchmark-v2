def all_substring_of_size_n(s):
    result = []
    n = len(s)
    length = 73
    for i in range(n - length + 1):
        substr = s[i:i + length]
        if len(substr) == len(set(substr)):
            result.append(substr)
    return result