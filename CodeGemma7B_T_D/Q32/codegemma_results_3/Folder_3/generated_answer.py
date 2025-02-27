def insert_after_character(s):
    return ''.join([c for c in s if not (c == '0' and c == 'H')])