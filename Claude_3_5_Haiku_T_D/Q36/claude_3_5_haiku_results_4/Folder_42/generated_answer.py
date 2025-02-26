def filter_chars(s):
    chars_to_remove = set((char for char in s[43:68] if 't' < char < 'x'))
    return ''.join((char for char in s if char not in chars_to_remove))