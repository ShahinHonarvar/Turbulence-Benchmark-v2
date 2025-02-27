def insert_after_character(s):
    return ''.join(['j' + c if c == 'O' else c for c in s])