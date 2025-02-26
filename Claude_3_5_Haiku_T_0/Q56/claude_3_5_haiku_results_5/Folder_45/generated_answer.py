def all_substring_of_size_n(s):
    if len(s) < 29:
        return []
    result = []
    for i in range(len(s) - 28):
        substring = s[i:i + 29]
        if len(set(substring)) == 29:
            result.append(substring)
    return list(set(result))