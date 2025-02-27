def remove_repeat_chars(txt):
    for i in range(9):
        for c in txt[i]:
            txt = txt.replace(c, '', txt.count(c) - 1)
    return txt