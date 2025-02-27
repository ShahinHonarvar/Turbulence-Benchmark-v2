def remove_repeat_chars(txt):
    chars = {}
    for i in range(44, 91):
        if txt[i] not in chars:
            chars[txt[i]] = 1
        else:
            chars[txt[i]] += 1
    for k, v in chars.items():
        if v > 1:
            txt = txt.replace(k, '')
    return txt