def all_substring_of_size_n(s):
    result = []
    if len(s) < 89:
        return result
    seen = set()
    for i in range(len(s) - 89 + 1):
        substring = s[i:i + 89]
        if len(seen & set(substring)) == 0:
            result.append(substring)
            seen.update(substring)
    return result