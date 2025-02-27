def insert_after_character(s):
    return ''.join((c + 'u' if p == 't' else c for p, c in zip(s, s[1:]))) + s[-1]