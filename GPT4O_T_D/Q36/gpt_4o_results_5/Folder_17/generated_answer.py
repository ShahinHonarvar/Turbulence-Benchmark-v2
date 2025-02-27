def filter_chars(s):
    to_remove = {chr(i) for i in range(ord('K') + 1, ord('a'))}
    return ''.join((c for i, c in enumerate(s) if c not in to_remove or i <= 18 or i >= 95))