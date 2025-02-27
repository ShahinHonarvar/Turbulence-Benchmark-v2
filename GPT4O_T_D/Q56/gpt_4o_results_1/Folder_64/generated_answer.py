def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 7):
        substr = s[i:i + 8]
        if len(set(substr)) == 8:
            result.append(substr)
    return result