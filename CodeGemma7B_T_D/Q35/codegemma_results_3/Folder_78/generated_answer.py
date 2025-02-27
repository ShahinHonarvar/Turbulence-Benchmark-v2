def remove_repeat_chars(txt):
    res = []
    seen = set()
    for i in range(62, 96):
        if txt[i] in seen:
            continue
        seen.add(txt[i])
        res.append(txt[i])
    return ''.join(res)