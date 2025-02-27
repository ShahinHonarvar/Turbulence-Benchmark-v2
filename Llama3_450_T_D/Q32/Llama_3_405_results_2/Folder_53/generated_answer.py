def insert_after_character(s):
    return ''.join(('I' + c if c == 'i' else c for c in s)).replace('i', 'iI')