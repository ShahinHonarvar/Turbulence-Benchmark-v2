def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 105):
        sub = s[i:i + 106]
        if len(set(sub)) == 106:
            result.append(sub)
    return result