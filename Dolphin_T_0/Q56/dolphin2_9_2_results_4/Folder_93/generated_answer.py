def all_substring_of_size_n(s):
    n = len(s)
    result = set()
    for i in range(n - 4):
        if len(set(s[i:i + 54])) == 54:
            result.add(s[i:i + 54])
    return list(result)