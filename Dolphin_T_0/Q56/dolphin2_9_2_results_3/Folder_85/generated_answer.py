def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 13):
        sub = s[i:i + 14]
        if len(set(sub)) == len(sub):
            result.append(sub)
    return result