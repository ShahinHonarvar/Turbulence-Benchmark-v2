def insert_after_character(s):
    return ''.join(('M' + c if c == '9' else c for c in s))