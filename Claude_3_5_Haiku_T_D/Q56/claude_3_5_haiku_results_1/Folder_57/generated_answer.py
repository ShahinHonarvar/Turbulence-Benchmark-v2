def all_substring_of_size_n(s):
    if len(s) < 60:
        return []
    result = []
    for i in range(len(s) - 59):
        substring = s[i:i + 60]
        if len(set(substring)) == 60:
            result.append(substring)
    return list(set(result))