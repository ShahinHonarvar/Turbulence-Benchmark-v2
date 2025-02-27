def filter_chars(text):
    res = []
    for i, ch in enumerate(text):
        if i >= 27 and i <= 85 and (ch >= 'c') and (ch <= 'i'):
            continue
        else:
            res.append(ch)
    return ''.join(res)