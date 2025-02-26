def all_substring_of_size_n(s):
    if len(s) < 56:
        return []
    result = set()
    for i in range(len(s) - 55):
        substring = s[i:i + 56]
        if len(set(substring)) == 56:
            result.add(substring)
    return list(result)