def all_substring_of_size_n(s):
    n = 49
    result = []
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            result.append(sub)
            result = [x for x in result if len(set(x)) == n]
    return result