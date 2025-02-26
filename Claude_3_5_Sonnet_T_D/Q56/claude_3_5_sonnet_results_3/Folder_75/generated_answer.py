def all_substring_of_size_n(s):
    result = set()
    n = len(s)
    for i in range(n - 15):
        substring = s[i:i + 16]
        if len(set(substring)) == 16:
            result.add(substring)
    return list(result)