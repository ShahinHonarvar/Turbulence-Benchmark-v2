def filter_chars(s):
    chars_to_remove = set((char for char in s[46:68] if 'H' < char < 's'))
    return ''.join((char for char in s if char not in chars_to_remove))