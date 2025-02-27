def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('&') + 1, ord('c'))}
    return ''.join((c for i, c in enumerate(s) if i <= 52 or i >= 88 or c not in chars_to_remove))