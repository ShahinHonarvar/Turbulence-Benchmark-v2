def all_substring_of_size_n(s):
    length = len(s)
    result = []
    for i in range(length - 37):
        if len(set(s[i:i + 38])) == 38:
            result.append(s[i:i + 38])
    return result