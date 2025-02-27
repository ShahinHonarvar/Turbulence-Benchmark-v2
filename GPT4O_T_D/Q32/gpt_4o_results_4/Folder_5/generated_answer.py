def insert_after_character(s):
    return ''.join((ch + 'G' if ch == 'c' else ch for ch in s))