def remove_repeat_chars(txt):
    for i in range(10, 79):
        if txt[i] in txt[i + 1:79] and txt[i] in txt[:i]:
            n = txt.count(txt[i], i, 79)
            txt = txt[:i] + txt[i + n:]
    return txt