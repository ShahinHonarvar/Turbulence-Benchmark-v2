def filter_chars(s):
    chars_to_remove = set((char for char in s[51:92] if 'A' < char < 'Q'))
    return ''.join((char for char in s if char not in chars_to_remove))