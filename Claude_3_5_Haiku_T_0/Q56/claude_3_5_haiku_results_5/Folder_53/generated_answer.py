def all_substring_of_size_n(s):
    if len(s) < 25:
        return []
    result = []
    for i in range(len(s) - 24):
        substring = s[i:i + 25]
        if len(set(substring)) == 25:
            result.append(substring)
    return list(set(result))