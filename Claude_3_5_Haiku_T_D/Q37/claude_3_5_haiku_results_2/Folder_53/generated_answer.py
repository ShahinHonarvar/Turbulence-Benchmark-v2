def filter_chars(s):
    removed_chars = set((char for char in s[83:100] if '*' <= char <= 'j'))
    return ''.join((char for char in s if char not in removed_chars))