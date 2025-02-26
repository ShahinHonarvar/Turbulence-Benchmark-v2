def filter_chars(s):
    chars_to_remove = set((char for char in s[78:87] if ';' < char < 'r'))
    return ''.join((char for char in s if char not in chars_to_remove))