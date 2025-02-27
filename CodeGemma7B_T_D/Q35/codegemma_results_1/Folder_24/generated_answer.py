from itertools import count

def remove_repeat_chars(s):
    seen = set()
    res = []
    for i, c in enumerate(s):
        if 13 < i < 91 and c in seen:
            continue
        seen.add(c)
        res.append(c)
    return ''.join(res)