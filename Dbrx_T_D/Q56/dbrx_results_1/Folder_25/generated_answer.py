def all_substring_of_size_n(s):
    result = []
    n = 67
    if len(s) < n or len(set(s)) < n:
        return result
    for i in range(len(s) - n + 1):
        substring = s[i:n + i]
        if len(set(substring)) == n:
            result.append(substring)
    return list(set(result))