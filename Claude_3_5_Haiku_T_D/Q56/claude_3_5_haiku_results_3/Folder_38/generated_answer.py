def all_substring_of_size_n(s):
    if len(s) < 35:
        return []
    result = set()
    for i in range(len(s) - 34):
        substring = s[i:i + 35]
        if len(set(substring)) == 35:
            result.add(substring)
    return list(result)