def filter_chars(s):
    chars_to_remove = {char for char in s[69:97] if 'V' < char < 'j'}
    return ''.join((char for char in s if char not in chars_to_remove))