def filter_chars(txt):
    res = ''
    for i in range(len(txt)):
        if i < 44 or i >= 68 or (txt[i] > 'W' and txt[i] < 'x'):
            res += txt[i]
    return res