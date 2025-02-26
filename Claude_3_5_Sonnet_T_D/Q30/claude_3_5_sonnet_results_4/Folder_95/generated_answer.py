def insert_before_character(s):
    return ''.join(['q' + c if c == 'j' else c for c in s])