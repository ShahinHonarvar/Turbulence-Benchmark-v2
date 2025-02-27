def all_substring_of_size_n(s):
    size = 94
    result = []
    for i in range(len(s) - size + 1):
        sub = s[i:i + size]
        if len(set(sub)) == size:
            result.append(sub)
    return result