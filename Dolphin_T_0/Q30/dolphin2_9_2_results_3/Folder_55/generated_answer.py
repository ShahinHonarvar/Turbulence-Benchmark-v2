def insert_before_character(string):
    return 'U'.join(('u' if c == 'u' else c for c in string))