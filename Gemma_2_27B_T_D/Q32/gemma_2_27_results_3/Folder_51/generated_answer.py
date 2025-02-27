def insert_after_character(s):
    return ''.join(['O' + c if c == 'o' else c for c in s])