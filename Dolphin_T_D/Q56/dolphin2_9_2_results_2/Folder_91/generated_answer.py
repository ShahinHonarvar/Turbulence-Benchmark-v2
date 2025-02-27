def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 5):
        if len(set(s[i:i + 6])) == 6:
            result.append(s[i:i + 6])
    return list(set(result))