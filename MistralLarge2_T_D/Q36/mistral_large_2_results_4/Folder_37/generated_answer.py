def filter_chars(s):
    to_remove = {char for char in s[44:59] if '/' < char < '6'}
    return ''.join((char for char in s if char not in to_remove))