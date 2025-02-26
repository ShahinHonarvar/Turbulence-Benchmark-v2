def filter_chars(s):
    chars_to_remove = set((char for char in s[284:484] if 'l' < char < 't'))
    return ''.join((char for char in s if char not in chars_to_remove))