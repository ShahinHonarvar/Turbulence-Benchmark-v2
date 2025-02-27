def all_substring_of_size_n(s):
    if len(s) < 14:
        return []
    result = set()
    for i in range(len(s) - 13):
        substring = ''.join(sorted(s[i:i + 14]))
        if len(substring) == 14:
            result.add(substring)
    return list(result)