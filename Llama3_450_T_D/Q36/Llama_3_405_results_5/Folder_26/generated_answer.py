def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 43 < i < 83 and ord(':') < ord(c) < ord('Q')]
    return ''.join((c for c in s if c not in chars_to_remove))