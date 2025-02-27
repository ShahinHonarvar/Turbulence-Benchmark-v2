def insert_before_character(s):
    return 'G' + s.replace('c', 'cG')[1:] if 'c' in s else s