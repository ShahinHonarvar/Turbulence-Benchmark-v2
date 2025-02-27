def filter_chars(s):
    chars_to_remove = set(s[34:68]).intersection(set([chr(i) for i in range(ord('W'), ord('x') + 1)]))
    return ''.join([char for char in s if char not in chars_to_remove])