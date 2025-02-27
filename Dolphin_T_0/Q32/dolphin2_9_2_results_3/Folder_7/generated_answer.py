def insert_after_character(s):
    return ' '.join((ch + 'H' if ch == ' ' else ch for ch in s))