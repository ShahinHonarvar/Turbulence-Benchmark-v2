def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 31):
        substr = s[i:i + 32]
        if len(set(substr)) == 32:
            result.append(substr)
    return result