def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 33):
        temp = s[i:i + 34]
        if len(set(temp)) == len(temp):
            result.append(temp)
    return result