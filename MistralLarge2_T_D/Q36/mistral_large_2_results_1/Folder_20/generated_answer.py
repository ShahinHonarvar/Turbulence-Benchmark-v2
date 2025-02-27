def filter_chars(s):
    chars_to_remove = set((char for char in s[13:40] if ':' < char < 'C'))
    return ''.join((char for char in s if char not in chars_to_remove))