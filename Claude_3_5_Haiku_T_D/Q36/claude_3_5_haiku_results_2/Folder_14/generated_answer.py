def filter_chars(s):
    chars_to_remove = set((char for char in s[42:56] if 'Z' < char < 'c'))
    return ''.join((char for char in s if char not in chars_to_remove))