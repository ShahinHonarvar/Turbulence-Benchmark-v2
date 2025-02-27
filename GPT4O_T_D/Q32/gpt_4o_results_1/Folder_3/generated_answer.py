def insert_after_character(s):
    return ''.join([ch + 'H' if ch == '0' else ch for ch in s])