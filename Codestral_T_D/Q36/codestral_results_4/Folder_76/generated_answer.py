def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('B') + 1, ord('Y'))}
    return ''.join((c for i, c in enumerate(s) if i < 669 or i >= 888 or c not in chars_to_remove))