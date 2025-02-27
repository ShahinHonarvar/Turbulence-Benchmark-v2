def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 19):
        sub = s[i:i + 20]
        if len(set(sub)) == 20:
            result.append(sub)
    return result