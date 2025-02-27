def insert_before_character(s):
    return ''.join(('u' if c == 'X' else x for x in s))