def filter_chars(s):
    chars_to_remove = {char for i, char in enumerate(s[11:33]) if '!' <= char <= '@'}
    return ''.join((char for char in s if char not in chars_to_remove))