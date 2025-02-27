def all_substring_of_size_n(s):
    result = []
    size = 63
    if len(s) < size:
        return result
    for i in range(len(s) - size + 1):
        sub = s[i:i + size]
        if len(sub) != len(set(sub)):
            continue
        result.append(sub)
    return result