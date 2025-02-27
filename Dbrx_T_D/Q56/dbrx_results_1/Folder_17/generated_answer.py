def all_substring_of_size_n(s):
    result = set()
    if len(s) < 37:
        return list(result)
    for i in range(len(s) - 36):
        substring = ''.join(sorted(s[i:i + 37]))
        result.add(substring)
    return list(result)