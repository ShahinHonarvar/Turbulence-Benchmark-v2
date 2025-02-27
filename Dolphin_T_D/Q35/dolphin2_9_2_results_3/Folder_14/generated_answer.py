def remove_repeat_chars(s):
    chars = set()
    result = ''
    for i, c in enumerate(s):
        if 2 <= i <= 5 and c in chars:
            s = s.replace(c, '')
        else:
            result += c
        if i >= 2 and i <= 5:
            chars.add(c)
    return result