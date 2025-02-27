def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 45):
        sub = s[i:i + 46]
        if len(set(sub)) != len(sub):
            continue
        result.append(sub)
    return result