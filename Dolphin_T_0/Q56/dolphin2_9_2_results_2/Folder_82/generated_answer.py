def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 99):
        ss = s[i:i + 100]
        if len(set(ss)) == 100 and ss not in result:
            result.append(ss)
    return result