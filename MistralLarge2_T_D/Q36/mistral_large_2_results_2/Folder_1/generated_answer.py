def filter_chars(s):
    to_remove = {char for char in s[69:87] if '#' < char < 'L'}
    return ''.join((char for char in s if char not in to_remove))