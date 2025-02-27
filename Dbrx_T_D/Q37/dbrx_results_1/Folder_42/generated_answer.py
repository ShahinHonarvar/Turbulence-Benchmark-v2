def filter_chars(s):
    start, end = (73, 74)
    chars_to_remove = [chr(i) for i in range(ord('U'), ord('l') + 1)]
    return ''.join((c for i, c in enumerate(s) if i < start or i > end or c not in chars_to_remove))