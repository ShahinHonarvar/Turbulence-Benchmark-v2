def all_substring_of_size_n(txt):
    result = []
    if len(txt) < 45:
        return result
    for i in range(len(txt) - 44):
        tmp = list(txt[i:i + 45])
        tmp.sort()
        strr = ''.join(tmp)
        if strr not in result:
            result.append(strr)
    return result