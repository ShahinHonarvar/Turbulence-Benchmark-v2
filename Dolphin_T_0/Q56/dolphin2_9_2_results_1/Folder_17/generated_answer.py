def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 36):
        sub = s[i:i + 37]
        if len(set(sub)) == 37:
            result.append(sub)
    return result