def insert_before_character(s):
    return ''.join(['t' + c if c == 'g' else c for c in s])