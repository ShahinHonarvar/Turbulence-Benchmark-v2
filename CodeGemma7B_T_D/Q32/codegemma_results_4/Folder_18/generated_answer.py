def insert_after_character(s):
    return ''.join((ch + 'l' if ch == 'K' else ch for ch in s))