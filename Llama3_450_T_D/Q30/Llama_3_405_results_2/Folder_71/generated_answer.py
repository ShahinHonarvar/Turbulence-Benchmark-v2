def insert_before_character(s):
    return ''.join(('S' + c if c == '2' else c for c in s))