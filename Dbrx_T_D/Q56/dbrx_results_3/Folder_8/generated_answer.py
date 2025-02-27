def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 29):
        if len(set(s[i:i + 30])) == 30:
            result.append(s[i:i + 30])
    return list(set(result))