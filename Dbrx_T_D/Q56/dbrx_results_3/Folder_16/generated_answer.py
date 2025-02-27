def all_substring_of_size_n(s):
    if len(s) < 124:
        return []
    result = set()
    for i in range(len(s) - 123):
        substring = ''.join(sorted(s[i:i + 124]))
        if len(substring) == 124:
            result.add(substring)
    return list(result)