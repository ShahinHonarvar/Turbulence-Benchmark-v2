def filter_chars(s):
    chars_to_remove = set(s[37:57]).intersection(set('6789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\\\]^_`'))
    return ''.join((char for char in s if char not in chars_to_remove))