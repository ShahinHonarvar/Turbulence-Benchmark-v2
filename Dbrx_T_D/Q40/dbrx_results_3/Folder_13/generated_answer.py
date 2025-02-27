def return_n_smallest_chars(s):
    s = sorted(s)
    result = []
    for i in range(min(31, len(s))):
        result.append(s[i])
    return result