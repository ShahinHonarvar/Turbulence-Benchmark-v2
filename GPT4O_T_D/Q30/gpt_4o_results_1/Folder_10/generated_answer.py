def insert_before_character(s):
    return ''.join(('v' + c if c == 'j' else c for c in s))