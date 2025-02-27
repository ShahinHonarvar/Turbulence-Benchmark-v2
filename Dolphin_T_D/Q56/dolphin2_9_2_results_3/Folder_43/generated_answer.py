def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n):
        for j in range(i + 86, n + 1):
            subs = s[i:j]
            if len(set(subs)) == len(subs):
                result.append(subs)
    return list(set(result))