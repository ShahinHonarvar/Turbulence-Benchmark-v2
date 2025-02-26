def insert_before_character(s):
    return ''.join(['M' + c if c == 'g' else c for c in s])