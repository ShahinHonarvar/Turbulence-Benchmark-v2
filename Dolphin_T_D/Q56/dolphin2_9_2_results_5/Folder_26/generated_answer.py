def all_substring_of_size_n(s):
    n = len(s)
    result = set()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if len(set(s[i:j + 3])) == 3:
                result.add(s[i:j + 3])
    return list(result)