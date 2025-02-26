def filter_chars(s):
    chars_to_remove = set((char for char in s[61:71] if '0' <= char <= '@'))
    return ''.join((char for char in s if char not in chars_to_remove))