def filter_chars(s):
    chars = set((chr(c) for c in range(ord('i'), ord('v') + 1)))
    return ''.join((c for i, c in enumerate(s) if not 11 <= i <= 72 or c not in chars))