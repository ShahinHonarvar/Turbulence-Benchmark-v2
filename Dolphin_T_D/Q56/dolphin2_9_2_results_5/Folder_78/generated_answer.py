def all_substring_of_size_n(s):
    n = len(s)
    result = []
    for i in range(n):
        for j in range(i + 49, n + 1):
            sub = s[i:j]
            if len(set(sub)) == len(sub):
                result.append(sub)
    return list(set(result))