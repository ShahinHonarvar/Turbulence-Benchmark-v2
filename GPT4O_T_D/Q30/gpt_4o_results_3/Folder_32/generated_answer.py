def insert_before_character(s):
    return ''.join(('uF' if ch == 'F' else ch for ch in s))