def all_substring_of_size_n(s):
    if len(s) < 45:
        return []
    result = set()
    for i in range(len(s) - 44):
        substring = s[i:i + 45]
        if len(set(substring)) == 45:
            result.add(substring)
    return list(result)