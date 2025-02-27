def remove_repeat_chars(txt):
    for c in txt[27:96]:
        while txt.count(c) > 1:
            txt = txt.replace(c, '', 1)
    return txt