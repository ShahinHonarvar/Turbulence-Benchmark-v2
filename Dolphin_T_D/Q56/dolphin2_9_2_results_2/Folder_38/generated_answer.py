def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 34):
        sub = s[i:i + 35]
        if len(set(sub)) == 35:
            result.append(sub)
    return result