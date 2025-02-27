def all_substring_of_size_n(s):
    if len(set(s)) < 79:
        return []
    result = []
    for i in range(len(s) - 78):
        if len(set(s[i:i + 79])) == 79:
            result.append(s[i:i + 79])
    return result