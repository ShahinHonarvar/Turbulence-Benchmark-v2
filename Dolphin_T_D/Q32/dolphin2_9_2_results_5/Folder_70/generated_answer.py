def insert_after_character(s):
    return ''.join(['V' if c == 'P' else c for c in s] + ['V'])