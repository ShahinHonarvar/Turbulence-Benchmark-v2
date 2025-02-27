def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 56 + 1):
        result.append(s[i:i + 56])
    return list(set(result))