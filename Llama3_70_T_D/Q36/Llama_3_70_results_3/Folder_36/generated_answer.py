def filter_chars(s):
    result = ''
    chars_to_remove = set()
    for c in s[283:484]:
        if 'l' < c < 't':
            chars_to_remove.add(c)
    for c in s:
        if c not in chars_to_remove:
            result += c
    return result