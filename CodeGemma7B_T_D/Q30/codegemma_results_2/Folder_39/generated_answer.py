def insert_before_character(s):
    return ''.join([ch + 'Q' if ch == 'm' else ch for ch in s])