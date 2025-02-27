def insert_after_character(s):
    return 'G'.join(('c' if c == 'c' else c + 'G' if G > c else c for c in s))