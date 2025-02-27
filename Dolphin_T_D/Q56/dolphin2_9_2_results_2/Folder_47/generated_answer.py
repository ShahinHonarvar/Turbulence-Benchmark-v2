def all_substring_of_size_n(s):
    n = len(s)
    result = []
    for i in range(n - 8):
        if len(set(s[i:i + 91])) == 91:
            result.append(s[i:i + 91])
    return result