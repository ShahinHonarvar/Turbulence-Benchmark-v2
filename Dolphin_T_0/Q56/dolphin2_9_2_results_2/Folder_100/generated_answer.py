def all_substring_of_size_n(s):
    n = len(s)
    result = []
    for i in range(n - 91):
        if len(set(s[i:i + 92])) == 92:
            result.append(s[i:i + 92])
    return result