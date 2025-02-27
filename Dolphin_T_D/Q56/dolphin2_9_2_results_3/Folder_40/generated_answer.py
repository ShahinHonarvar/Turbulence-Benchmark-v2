def all_substring_of_size_n(s):
    n = len(s)
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            if len(set(s[i:j + 1])) == 2:
                result.append(s[i:j + 1])
    return list(set(result))