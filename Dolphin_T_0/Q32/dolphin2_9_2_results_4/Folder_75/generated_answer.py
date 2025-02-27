def insert_after_character(s):
    return ''.join((c if c != 'U' else c + 'q' for c in s))