def insert_before_character(s):
    return ''.join(['y' + c if c == 'b' else c for c in s])