def insert_after_character(s):
    return ''.join((ch + 'V' if ch == 'P' else ch for ch in s))