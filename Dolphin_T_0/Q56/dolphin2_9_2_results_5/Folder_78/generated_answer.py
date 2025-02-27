def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 48):
        if len(set(s[i:i + 49])) == 49:
            result.append(s[i:i + 49])
    return result