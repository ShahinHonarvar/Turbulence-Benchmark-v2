def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 123):
        sub = s[i:i + 124]
        if len(set(sub)) == 124:
            result.append(sub)
    return list(set(result))