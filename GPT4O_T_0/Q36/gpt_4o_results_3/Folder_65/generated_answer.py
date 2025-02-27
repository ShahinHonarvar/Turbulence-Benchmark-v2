def filter_chars(s):
    to_remove = {chr(i) for i in range(ord('G'), ord('O'))}
    return ''.join((c for i, c in enumerate(s) if c not in to_remove or i <= 58 or i >= 82))