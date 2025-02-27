def all_substring_of_size_n(s):
    length = 53
    result = []
    for i in range(len(s) - length + 1):
        sub = s[i:i + length]
        if len(set(sub)) == length:
            result.append(sub)
    return result