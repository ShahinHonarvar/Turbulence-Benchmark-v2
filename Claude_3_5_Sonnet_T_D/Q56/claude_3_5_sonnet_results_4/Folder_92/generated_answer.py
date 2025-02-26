def all_substring_of_size_n(s):
    result = set()
    n = len(s)
    for i in range(n - 8):
        substring = s[i:i + 9]
        if len(set(substring)) == 9:
            result.add(substring)
    return list(result)