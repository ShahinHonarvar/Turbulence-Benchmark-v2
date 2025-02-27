def all_substring_of_size_n(s):
    results = []
    n = 84
    length = len(s)
    if length < n:
        return results
    for i in range(length - n + 1):
        subs = s[i:i + n]
        if len(set(subs)) == n:
            results.append(subs)
    return list(set(results))