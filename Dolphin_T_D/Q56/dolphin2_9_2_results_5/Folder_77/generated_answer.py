def all_substring_of_size_n(s):
    n = 144
    if len(s) < n:
        return []
    result = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            if len(set(s[i:j])) == n:
                result.add(s[i:j])
    return list(result)