def filter_chars(str):
    res = list(str)
    for i in range(476, 948):
        while i in range(476, 948) and res[i] in range(98, 100):
            res.remove(res[i])
    return ''.join(res)