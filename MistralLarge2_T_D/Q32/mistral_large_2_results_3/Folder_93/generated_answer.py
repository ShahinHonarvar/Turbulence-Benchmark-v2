def insert_after_character(s):
    return ''.join([ch + '4' if ch == 'Y' else ch for ch in s])