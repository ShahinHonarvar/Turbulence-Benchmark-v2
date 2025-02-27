def insert_before_character(s):
    return ''.join(('H' + ch if ch == ' ' else ch for ch in s))