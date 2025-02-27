def all_substring_of_size_n(s):
    result = []
    n = len(s)
    if n < 49:
        return result
    for i in range(n - 48):
        substring = s[i:i + 49]
        if len(set(substring)) == 49:
            result.append(substring)
    return result