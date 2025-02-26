def filter_chars(s):
    chars_to_remove = set((char for char in s[52:76] if '5' < char < 'f'))
    return ''.join((char for char in s if char not in chars_to_remove))