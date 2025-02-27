def filter_chars(s):
    chars_to_remove = {char for char in s[170:195] if '!' < char < '}'}
    return ''.join((char for char in s if char not in chars_to_remove))