def filter_chars(s):
    if len(s) < 7:
        return s
    chars_to_remove = set((char for char in s[5:7] if 'G' <= char <= 'p'))
    return ''.join((char for char in s if char not in chars_to_remove))