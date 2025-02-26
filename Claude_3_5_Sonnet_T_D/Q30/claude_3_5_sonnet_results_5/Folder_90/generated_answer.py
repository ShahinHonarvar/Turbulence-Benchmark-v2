def insert_before_character(s):
    return ''.join(['F' + c if c == 'U' else c for c in s])