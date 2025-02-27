def filter_chars(s):
    to_remove = set((char for char in s[33:84] if 'm' < char < 'w'))
    return ''.join((char for char in s if char not in to_remove))