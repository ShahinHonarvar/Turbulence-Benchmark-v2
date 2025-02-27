def filter_chars(s):
    chars_to_remove = [chr(x) for x in range(ord('%') + 1, ord('q'))]
    return ''.join([c for c in s if c not in chars_to_remove[61:88]])