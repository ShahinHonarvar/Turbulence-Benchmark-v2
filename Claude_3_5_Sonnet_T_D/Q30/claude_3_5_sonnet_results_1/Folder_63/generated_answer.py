def insert_before_character(s):
    return ''.join(['R' + c if c == '5' else c for c in s])