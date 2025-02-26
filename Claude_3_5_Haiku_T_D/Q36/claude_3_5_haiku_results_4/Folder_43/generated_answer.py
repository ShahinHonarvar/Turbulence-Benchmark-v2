def filter_chars(s):
    chars_to_remove = set((char for char in s[28:75] if 'A' < char < 'i'))
    return ''.join((char for char in s if char not in chars_to_remove))