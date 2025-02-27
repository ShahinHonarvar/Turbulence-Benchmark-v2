def all_substring_of_size_n(s):
    if len(s) < 60:
        return []
    result = []
    for i in range(len(s) - 59):
        if len(set(s[i:i + 60])) == 60:
            result.append(s[i:i + 60])
    return result