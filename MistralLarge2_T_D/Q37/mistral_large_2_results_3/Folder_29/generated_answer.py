def filter_chars(s):
    chars_to_remove = set((char for char in s[12:89] if '&' <= char <= 'v'))
    return ''.join((char for char in s if char not in chars_to_remove))