def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 148):
        if len(set(s[i:i + 149])) == 149:
            result.append(s[i:i + 149])
    return result