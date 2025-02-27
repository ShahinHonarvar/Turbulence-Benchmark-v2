def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 53):
        if len(set(s[i:i + 54])) == 54:
            result.append(s[i:i + 54])
    return result