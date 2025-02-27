def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(28, 66) if 'O' <= chr(i) <= 'd'])
    return ''.join([c for c in s if c not in chars_to_remove])