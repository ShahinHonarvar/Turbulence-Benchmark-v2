def remove_repeat_chars(s):
    seen = set()
    res = []
    for char in s:
        if 60 < ord(char) < 200 and char in seen:
            continue
        seen.add(char)
        res.append(char)
    return ''.join(res)