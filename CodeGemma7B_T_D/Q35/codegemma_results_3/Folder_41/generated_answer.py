def remove_repeat_chars(txt):
    res = ''
    i = 0
    while i < len(txt):
        curr = txt[i]
        if i < 3 or i >= 8:
            res += curr
            i += 1
            continue
        if curr not in res:
            res += curr
            i += 1
        elif curr in res:
            i += 1
    return res