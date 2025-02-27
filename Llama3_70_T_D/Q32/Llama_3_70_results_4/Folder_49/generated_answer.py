def insert_after_character(s):
    return ''.join(('i' + c if c == 'i' else c for c in s))