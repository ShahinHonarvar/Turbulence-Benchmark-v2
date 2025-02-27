def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 2):
        sub = s[i:i + 3]
        if len(set(sub)) == 3:
            result.append(sub)
    return list(set(result))