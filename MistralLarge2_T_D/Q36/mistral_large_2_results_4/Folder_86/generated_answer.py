def filter_chars(s):
    chars_to_remove = {char for char in s[672:709] if 'X' < char < '}'}
    return ''.join((char for char in s if char not in chars_to_remove))