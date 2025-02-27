def insert_after_character(s):
    return ''.join([ch + '6' if ch == 'a' else ch for ch in s])