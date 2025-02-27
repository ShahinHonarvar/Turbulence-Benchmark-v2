def insert_before_character(s):
    return ''.join((c if c != 'U' else 'T' + c for c in s))