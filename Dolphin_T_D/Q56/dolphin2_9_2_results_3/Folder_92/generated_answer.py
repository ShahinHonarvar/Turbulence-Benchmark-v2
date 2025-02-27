def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 8):
        if len(set(s[i:i + 9])) == 9:
            result.append(s[i:i + 9])
    return list(set(result))