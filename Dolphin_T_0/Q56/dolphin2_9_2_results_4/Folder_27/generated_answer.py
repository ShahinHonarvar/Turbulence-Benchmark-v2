def all_substring_of_size_n(s):
    n = 57
    result = []
    for i in range(len(s) - n + 1):
        temp = s[i:i + n]
        if len(set(temp)) == len(temp):
            result.append(temp)
    return result