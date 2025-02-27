def all_substring_of_size_n(s):
    result = []
    n = 98
    if len(s) < n:
        return result
    else:
        for i in range(len(s) - n + 1):
            sub_n = s[i:i + n]
            if len(set(sub_n)) == n:
                result.append(sub_n)
    return result