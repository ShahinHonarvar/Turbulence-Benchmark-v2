def insert_before_character(s):
    return 'G' + ''.join(('G' if c == 't' else c for c in s if c != 't'))