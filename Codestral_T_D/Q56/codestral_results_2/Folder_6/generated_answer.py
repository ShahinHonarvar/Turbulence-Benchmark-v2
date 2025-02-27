def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 23 + 1):
        sub = s[i:i + 23]
        if len(set(sub)) == 23:
            result.append(sub)
    return result