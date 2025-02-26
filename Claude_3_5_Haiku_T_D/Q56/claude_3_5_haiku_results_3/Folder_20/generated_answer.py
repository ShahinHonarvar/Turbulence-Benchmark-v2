def all_substring_of_size_n(s):
    result = []
    n = 50
    if len(s) < n:
        return result
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n and substring not in result:
            result.append(substring)
    return result