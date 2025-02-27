def filter_chars(s):
    to_remove = {char for char in s[42:68] if 't' < char < 'x'}
    return ''.join((char for char in s if char not in to_remove))