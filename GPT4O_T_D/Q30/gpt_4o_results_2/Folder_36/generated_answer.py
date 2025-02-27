def insert_before_character(s):
    return ''.join(('H' + ch if ch == 'A' else ch for ch in s))