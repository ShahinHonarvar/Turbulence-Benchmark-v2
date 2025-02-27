def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 99):
        if len(set(s[i:i + 100])) == 100:
            result.append(s[i:i + 100])
    return result