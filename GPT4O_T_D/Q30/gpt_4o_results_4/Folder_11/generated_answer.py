def insert_before_character(s):
    return ''.join(('tg' if ch == 'g' else ch for ch in s))