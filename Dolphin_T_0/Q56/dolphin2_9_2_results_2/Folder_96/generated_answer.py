def all_substring_of_size_n(s):
    result = []
    if len(s) < 2:
        return []
    for i in range(len(s) - 2):
        sub = s[i:i + 3]
        if len(set(sub)) == 3 and sub not in result:
            result.append(sub)
    return result