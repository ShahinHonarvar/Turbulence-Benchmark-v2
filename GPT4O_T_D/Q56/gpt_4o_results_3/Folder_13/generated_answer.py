def all_substring_of_size_n(s):
    result = []
    n = len(s)
    target_length = 53
    if n < target_length:
        return result
    for i in range(n - target_length + 1):
        substr = s[i:i + target_length]
        if len(set(substr)) == target_length:
            result.append(substr)
    return result