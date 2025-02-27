def all_substring_of_size_n(s: str):
    result = []
    n = 99
    if len(s) < n:
        return result
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            result.append(substring)
    return result