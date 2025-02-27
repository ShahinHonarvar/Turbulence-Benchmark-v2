def insert_before_character(s):
    return ''.join(('1' + ch if ch == 'j' else ch for ch in s))