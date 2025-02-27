def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 24):
        substr = s[i:i + 25]
        if len(substr) == 25 and len(set(substr)) == 25:
            result.append(substr)
    return list(set(result))