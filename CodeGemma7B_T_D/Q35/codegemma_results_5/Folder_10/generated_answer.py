def remove_repeat_chars(str1):
    res = []
    for i in range(len(str1)):
        if i >= 36 and i < 54:
            if str1[i] not in res:
                res.append(str1[i])
    return ''.join(res)