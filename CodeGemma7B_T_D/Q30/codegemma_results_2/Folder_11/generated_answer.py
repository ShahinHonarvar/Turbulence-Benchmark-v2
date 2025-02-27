def insert_before_character(s):
    return ''.join((ch + 't' if ch == 'g' else ch for ch in s))