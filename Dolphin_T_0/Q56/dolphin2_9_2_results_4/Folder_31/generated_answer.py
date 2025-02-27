def all_substring_of_size_n(s):
    if len(s) < 46:
        return []
    result = []
    for i in range(len(s) - 45):
        if len(set(s[i:i + 46])) == 46:
            result.append(s[i:i + 46])
    return result