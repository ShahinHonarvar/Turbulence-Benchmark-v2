def insert_after_character(str):
    return ''.join((ch + 's' if ch == 'H' else ch for ch in str))