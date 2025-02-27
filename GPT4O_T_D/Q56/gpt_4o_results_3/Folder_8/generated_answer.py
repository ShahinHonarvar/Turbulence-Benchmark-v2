def all_substring_of_size_n(s):
    n = 30
    res = []
    if len(s) < n:
        return res
    seen = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n and substring not in seen:
            res.append(substring)
            seen.add(substring)
    return res