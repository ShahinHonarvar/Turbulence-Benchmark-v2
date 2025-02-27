def insert_before_character(s):
    return ''.join(('m' + ch if ch == 'F' else ch for ch in s))