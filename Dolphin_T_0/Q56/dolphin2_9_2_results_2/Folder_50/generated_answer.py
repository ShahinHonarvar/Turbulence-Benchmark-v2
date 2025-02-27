def all_substring_of_size_n(s):
    if len(set(s)) < 11 or len(s) < 11:
        return []
    result = []
    for i in range(len(s) - 10):
        if len(set(s[i:i + 11])) == 11 and s[i:i + 11] not in result:
            result.append(s[i:i + 11])
    return result