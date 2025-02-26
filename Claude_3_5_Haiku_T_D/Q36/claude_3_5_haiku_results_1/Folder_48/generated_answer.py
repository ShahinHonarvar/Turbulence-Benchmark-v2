def filter_chars(s):
    chars_to_remove = set((char for char in s[155:222] if 'A' < char < 'f'))
    return ''.join((char for char in s if char not in chars_to_remove))