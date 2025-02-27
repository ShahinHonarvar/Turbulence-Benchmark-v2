def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('G'), ord('O'))}
    return ''.join((c for i, c in enumerate(s) if c not in chars_to_remove or not 58 < i < 82))