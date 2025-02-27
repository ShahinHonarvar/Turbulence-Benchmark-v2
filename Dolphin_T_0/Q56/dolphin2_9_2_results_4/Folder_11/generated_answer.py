def all_substring_of_size_n(s):
    if len(set(s)) < 78:
        return []
    result = []
    for i in range(len(s) - 77):
        sub = s[i:i + 78]
        if len(set(sub)) == 78:
            result.append(sub)
    return result