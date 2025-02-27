def all_substring_of_size_n(s):
    length = len(s)
    result = []
    for i in range(length - 49):
        sub = s[i:i + 50]
        if len(set(sub)) == len(sub):
            result.append(sub)
    return result