def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 37):
        sub = s[i:i + 38]
        if len(set(sub)) == 38:
            result.append(sub)
    return result