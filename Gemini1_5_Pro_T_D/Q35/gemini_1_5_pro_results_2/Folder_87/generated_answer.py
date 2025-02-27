def remove_repeat_chars(s):
    seen = set()
    res = []
    for i, c in enumerate(s):
        if 20 < i < 43:
            if c in seen:
                continue
            elif s.count(c, 21, 43) > 1:
                seen.add(c)
                continue
            else:
                res.append(c)
        else:
            res.append(c)
    return ''.join(res)