def filter_chars(s):
    chars_to_remove = ''
    for char in s[86:93]:
        if '!' <= char <= 's':
            chars_to_remove += char
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s