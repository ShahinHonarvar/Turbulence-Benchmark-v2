def all_substring_of_size_n(s):
    if len(s) < 106:
        return []
    result = []
    for i in range(len(s) - 105):
        substring = s[i:i + 106]
        if len(set(substring)) == 106:
            result.append(substring)
    return result