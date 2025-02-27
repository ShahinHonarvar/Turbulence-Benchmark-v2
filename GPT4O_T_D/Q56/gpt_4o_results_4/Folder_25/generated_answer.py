def all_substring_of_size_n(s):
    result = []
    n = 67
    length = len(s)
    if length < n:
        return result
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            result.append(substring)
    return result