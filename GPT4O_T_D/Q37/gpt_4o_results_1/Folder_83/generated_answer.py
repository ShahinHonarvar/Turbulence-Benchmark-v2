def filter_chars(s):
    if len(s) < 30:
        return s
    chars_to_remove = set()
    for char in s[29:80]:
        if 'K' <= char <= 'z':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))