def insert_after_character(s):
    return ''.join(['S' if c == ' ' else c for c in s]).replace('S', 'US')