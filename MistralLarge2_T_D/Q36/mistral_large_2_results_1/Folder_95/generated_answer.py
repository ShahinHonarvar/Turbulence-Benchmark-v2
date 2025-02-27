def filter_chars(s):
    to_remove = {char for char in s[56:86] if '+' < char < 'w'}
    return ''.join((char for char in s if char not in to_remove))