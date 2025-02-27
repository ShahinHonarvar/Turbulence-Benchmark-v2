def all_substring_of_size_n(s):
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 18, n + 1):
            if len(set(s[i:j])) == 18:
                result.add(s[i:j])
    return list(result)