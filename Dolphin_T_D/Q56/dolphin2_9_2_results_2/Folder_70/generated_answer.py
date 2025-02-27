def all_substring_of_size_n(s):
    if len(set(s)) < 12:
        return []
    result = []
    for i in range(len(s) - 11):
        sub = s[i:i + 12]
        if len(set(sub)) == 12:
            result.append(sub)
    return result