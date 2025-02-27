def insert_after_character(s):
    return ''.join(('a' + ch if ch == 'a' else ch for ch in s))