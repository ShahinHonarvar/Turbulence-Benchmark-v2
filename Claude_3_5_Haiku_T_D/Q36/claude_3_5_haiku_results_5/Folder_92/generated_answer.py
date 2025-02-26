def filter_chars(s):
    chars_to_remove = set(s[2:6])
    return ''.join((char for char in s if char not in chars_to_remove))