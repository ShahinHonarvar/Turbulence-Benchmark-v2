def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 16):
        sub = s[i:i + 17]
        if len(set(sub)) == 17:
            result.append(sub)
    result = list(set(result))
    if not result:
        return []
    else:
        return result