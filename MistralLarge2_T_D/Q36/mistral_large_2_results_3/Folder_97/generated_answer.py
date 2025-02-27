def filter_chars(s):
    to_remove = {char for char in s[309:591] if 'S' < char < 'm'}
    return ''.join((char for char in s if char not in to_remove))