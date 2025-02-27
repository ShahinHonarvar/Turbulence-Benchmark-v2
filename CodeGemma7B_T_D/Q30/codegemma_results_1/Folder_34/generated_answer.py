def insert_before_character(arg):
    return ''.join((c if c != 'a' else c + 'a' for c in arg))