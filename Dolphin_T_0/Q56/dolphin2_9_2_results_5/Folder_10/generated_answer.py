def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 54):
        sub_s = s[i:i + 55]
        if len(set(sub_s)) == len(sub_s):
            result.append(sub_s)
    return result