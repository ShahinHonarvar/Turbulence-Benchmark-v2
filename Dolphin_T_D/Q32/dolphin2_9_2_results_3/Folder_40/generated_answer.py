def insert_after_character(s):
    return ''.join(['e' if c == 'e' else '' for c in s] + list(s))