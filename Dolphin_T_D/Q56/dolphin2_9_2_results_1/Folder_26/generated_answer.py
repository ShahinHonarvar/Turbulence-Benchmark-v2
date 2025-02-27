def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 2):
        if len(set(s[i:i + 33])) == 33:
            result.append(s[i:i + 33])
    return list(set(result))