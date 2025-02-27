def all_substring_of_size_n(s):
    n = len(s)
    if n < 86:
        return []
    result = set()
    for i in range(n - 85):
        substring = s[i:i + 86]
        if len(set(substring)) == 86:
            result.add(substring)
    return list(result)