def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 9):
        sub_s = s[i:i + 10]
        if len(set(sub_s)) == 10:
            result.append(sub_s)
    return result