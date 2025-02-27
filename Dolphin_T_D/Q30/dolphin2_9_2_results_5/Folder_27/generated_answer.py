def insert_before_character(s):
    return 'j'.join((n if n != 'N' else 'jN' for n in s))