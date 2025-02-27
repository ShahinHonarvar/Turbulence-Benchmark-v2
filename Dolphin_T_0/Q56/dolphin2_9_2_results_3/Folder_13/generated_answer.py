def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 52):
        sub = s[i:i + 53]
        if len(set(sub)) == 53:
            result.append(sub)
    return result