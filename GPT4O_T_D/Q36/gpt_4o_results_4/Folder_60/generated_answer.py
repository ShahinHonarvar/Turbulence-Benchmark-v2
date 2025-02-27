def filter_chars(s):
    to_remove = set((chr(i) for i in range(ord('g'), ord('o'))))
    return ''.join((c for c in s if c not in to_remove or s.index(c) <= 23 or s.index(c) >= 83))