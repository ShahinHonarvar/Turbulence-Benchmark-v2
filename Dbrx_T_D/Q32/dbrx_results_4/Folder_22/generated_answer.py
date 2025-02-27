def insert_after_character(s):
    return ''.join((c if c != 'U' else 'UU' for c in s))