def all_substring_of_size_n(s):
    result = []
    n = 88
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            result.append(sub)
    return result