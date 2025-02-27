def filter_chars(s):
    chars_to_remove = {char for char in s[31:70] if 'B' < char < 'v'}
    return ''.join((char for char in s if char not in chars_to_remove))