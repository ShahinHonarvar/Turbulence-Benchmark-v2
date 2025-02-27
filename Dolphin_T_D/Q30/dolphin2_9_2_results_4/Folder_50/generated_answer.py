def insert_before_character(s):
    return ''.join(['u' if c == 't' else c for c in s]) + 'u'