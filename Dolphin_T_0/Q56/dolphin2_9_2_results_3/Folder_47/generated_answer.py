def all_substring_of_size_n(s):
    n = 91
    result = []
    for i in range(len(s) - n + 1):
        if len(set(s[i:i + n])) == n and s[i:i + n] not in result:
            result.append(s[i:i + n])
    return result