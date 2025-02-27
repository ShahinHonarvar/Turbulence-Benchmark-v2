def filter_chars(s):
    chars_to_remove = set((char for char in s[31:73] if 'M' < char < 'j'))
    return ''.join((char for char in s if char not in chars_to_remove))