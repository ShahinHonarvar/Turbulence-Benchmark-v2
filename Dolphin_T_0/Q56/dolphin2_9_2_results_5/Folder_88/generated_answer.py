def all_substring_of_size_n(s):
    if len(set(s)) < 68:
        return []
    result = []
    for i in range(len(s) - 67):
        if len(set(s[i:i + 68])) == 68:
            result.append(s[i:i + 68])
    return result