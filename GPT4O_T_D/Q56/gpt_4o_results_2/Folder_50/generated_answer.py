def all_substring_of_size_n(s):
    result = set()
    n = len(s)
    for i in range(n - 10):
        substring = s[i:i + 11]
        if len(set(substring)) == 11:
            result.add(substring)
    return list(result)