def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 11 + 1):
        sub_s = s[i:i + 11]
        if len(set(sub_s)) == 11:
            result.append(sub_s)
    return result