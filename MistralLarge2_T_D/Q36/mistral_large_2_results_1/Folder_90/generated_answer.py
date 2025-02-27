def filter_chars(s):
    to_remove = {char for char in s[344:874] if 'f' < char < '~'}
    return ''.join((char for char in s if char not in to_remove))