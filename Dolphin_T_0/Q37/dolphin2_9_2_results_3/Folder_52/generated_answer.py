def filter_chars(string):
    chars_to_remove = [c for c in string[54:84] if 'j' <= c <= 'v']
    return ''.join([c for c in string if c not in chars_to_remove])