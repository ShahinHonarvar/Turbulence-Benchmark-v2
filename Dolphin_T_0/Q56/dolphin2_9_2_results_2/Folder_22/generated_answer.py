def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n):
        for j in range(i + 22, n):
            sub = s[i:j]
            if len(set(sub)) == len(sub):
                result.append(sub)
    return result