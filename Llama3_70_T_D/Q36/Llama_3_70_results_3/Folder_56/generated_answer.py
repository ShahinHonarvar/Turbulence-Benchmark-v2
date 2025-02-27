def filter_chars(s):
    temp = ''
    chars_to_remove = set()
    for c in s[31:50]:
        if '/' < c < 'J':
            chars_to_remove.add(c)
    for c in s:
        if c not in chars_to_remove:
            temp += c
    return temp