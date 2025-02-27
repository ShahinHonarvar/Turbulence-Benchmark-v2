def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 141):
        sub = s[i:i + 142]
        if len(set(sub)) == len(sub):
            result.append(sub)
    return result