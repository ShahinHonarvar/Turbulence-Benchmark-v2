def insert_before_character(s):
    return ''.join(('I' + c if c == 'I' else c for c in s))