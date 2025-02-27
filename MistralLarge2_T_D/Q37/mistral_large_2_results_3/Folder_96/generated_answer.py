def filter_chars(s):
    to_remove = {char for i, char in enumerate(s) if 86 <= i <= 92 and '!' <= char <= 's'}
    return ''.join((char for char in s if char not in to_remove))