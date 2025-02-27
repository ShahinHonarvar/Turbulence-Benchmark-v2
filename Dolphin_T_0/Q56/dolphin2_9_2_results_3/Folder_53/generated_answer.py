def all_substring_of_size_n(s):
    if len(s) < 25:
        return []
    result = []
    i = 0
    while i <= len(s) - 25:
        sub = s[i:i + 25]
        if len(set(sub)) == 25:
            result.append(sub)
        i += 1
    return result