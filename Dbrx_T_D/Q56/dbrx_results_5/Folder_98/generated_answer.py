def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 9):
        if len(set(s[i:i + 10])) == 10:
            result.append(s[i:i + 10])
    return list(set(result))