def insert_after_character(s):
    return ''.join([ch + 'N' if ch == 'B' else ch for ch in s])