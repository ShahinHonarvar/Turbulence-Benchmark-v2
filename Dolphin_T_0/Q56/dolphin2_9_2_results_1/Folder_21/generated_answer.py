def all_substring_of_size_n(s):
    n = 106
    result = []
    for i in range(len(s) - n + 1):
        if len(set(s[i:i + n])) == n:
            result.append(s[i:i + n])
    return result