def insert_after_character(s):
    return ''.join((ch + 'h' if ch == '5' else ch for ch in s))