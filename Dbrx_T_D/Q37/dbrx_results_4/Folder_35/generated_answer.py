def filter_chars(s):
    chars_to_remove = set(range(ord('('), ord(']') + 1))
    return ''.join((c for i, c in enumerate(s) if i < 155 or i > 403 or ord(c) not in chars_to_remove))