def insert_before_character(s):
    return '0'.join((c if c != 'e' else '0' + c for c in s))