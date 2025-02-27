def filter_chars(s):
    chars_to_remove = {char for char in s[81:86] if '!' < char < 's'}
    return ''.join((char for char in s if char not in chars_to_remove))