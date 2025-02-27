def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 85):
        if len(set(s[i:i + 86])) == 86:
            result.append(s[i:i + 86])
    return result