def all_substring_of_size_n(s):
    result = []
    n = 68
    if len(s) < n:
        return result
    seen = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(seen & set(substring)) == 0:
            result.append(substring)
            seen.update(substring)
    return result