def filter_chars(s):
    to_remove = {char for char in s[46:68] if 'H' < char < 's'}
    return ''.join([char for char in s if char not in to_remove])