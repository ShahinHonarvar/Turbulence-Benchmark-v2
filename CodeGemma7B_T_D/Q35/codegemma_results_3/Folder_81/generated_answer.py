def remove_repeat_chars(str):
    s = set()
    res = []
    for i in range(20, 200):
        if str[i] not in s:
            res.append(str[i])
            s.add(str[i])
    return ''.join(res)