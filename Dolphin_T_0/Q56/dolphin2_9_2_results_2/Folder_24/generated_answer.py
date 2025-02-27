def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 49):
        sub = s[i:i + 51]
        if len(set(sub)) == 51:
            result.append(sub)
    return result if len(result) > 0 else []