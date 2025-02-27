def insert_before_character(s):
    return ''.join(('W' + c if c == '6' else c for c in s))