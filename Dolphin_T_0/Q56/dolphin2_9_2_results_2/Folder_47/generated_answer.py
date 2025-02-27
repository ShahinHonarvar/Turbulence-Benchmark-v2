def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 90):
        sub = s[i:i + 91]
        if len(set(sub)) == len(sub):
            result.append(sub)
    return result