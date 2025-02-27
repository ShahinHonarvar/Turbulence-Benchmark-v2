def filter_chars(s):
    chars_to_remove = set()
    for char in s[477:985]:
        if ',' <= char <= 'V':
            chars_to_remove.add(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s