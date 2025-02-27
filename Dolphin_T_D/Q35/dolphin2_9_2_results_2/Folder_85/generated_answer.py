def remove_repeat_chars(s):
    chars = set()
    result = ''
    for i, c in enumerate(s):
        if i < 1 or i > 8:
            result += c
        elif c not in chars:
            chars.add(c)
            result += c
    return result