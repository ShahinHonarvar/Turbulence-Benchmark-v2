def insert_before_character(s):
    return ''.join(['G' + c if c == 't' else c for c in s])