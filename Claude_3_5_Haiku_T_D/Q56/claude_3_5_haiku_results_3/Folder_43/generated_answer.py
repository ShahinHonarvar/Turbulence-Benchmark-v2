def all_substring_of_size_n(s):
    if len(s) < 86:
        return []
    result = set()
    for i in range(len(s) - 85):
        substring = s[i:i + 86]
        if len(set(substring)) == 86:
            result.add(substring)
    return list(result)