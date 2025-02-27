def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 119):
        sub = s[i:i + 120]
        if len(set(sub)) == 120:
            result.append(sub)
    return result