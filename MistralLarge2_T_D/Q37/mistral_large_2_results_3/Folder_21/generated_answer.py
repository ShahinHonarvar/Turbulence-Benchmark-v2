def filter_chars(s):
    to_remove = {char for i, char in enumerate(s) if 603 <= i <= 759 and 'Q' <= char <= 'h'}
    return ''.join((char for char in s if char not in to_remove))