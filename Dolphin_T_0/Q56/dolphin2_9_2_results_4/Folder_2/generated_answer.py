def all_substring_of_size_n(s):
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 56, n):
            if len(set(s[i:j])) == 56:
                result.add(s[i:j])
    return list(result)