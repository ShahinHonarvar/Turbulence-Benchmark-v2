def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(25, 98) if 'm' <= chr(i) <= 'w']
    return ''.join([c for c in s if c not in chars_to_remove])