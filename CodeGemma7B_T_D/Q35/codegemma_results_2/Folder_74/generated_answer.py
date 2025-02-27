def remove_repeat_chars(txt):
    seen = set()
    res = []
    for i in range(len(txt)):
        if 69 < i < 97 and txt[i] in seen:
            continue
        seen.add(txt[i])
        res.append(txt[i])
    return ''.join(res)