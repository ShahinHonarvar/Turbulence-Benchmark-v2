def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 16):
        if len(set(s[i:i + 17])) == 17:
            result.append(s[i:i + 17])
    return list(set(result))