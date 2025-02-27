def insert_after_character(s):
    return ''.join([ch + 'K' if ch == ' ' else ch for ch in s])