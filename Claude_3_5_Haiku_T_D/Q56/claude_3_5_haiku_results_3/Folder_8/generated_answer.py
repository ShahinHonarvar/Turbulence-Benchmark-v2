def all_substring_of_size_n(s):
    if len(s) < 30:
        return []
    result = []
    for i in range(len(s) - 29):
        substring = s[i:i + 30]
        if len(set(substring)) == 30:
            result.append(substring)
    return list(set(result))