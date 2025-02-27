def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 80):
        substr = s[i:i + 81]
        if len(set(substr)) == 81:
            result.append(substr)
    return result