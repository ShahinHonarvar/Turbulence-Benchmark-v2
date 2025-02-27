def all_substring_of_size_n(s):
    result = []
    n = 42
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            result.append(substring)
    return list(set(result))