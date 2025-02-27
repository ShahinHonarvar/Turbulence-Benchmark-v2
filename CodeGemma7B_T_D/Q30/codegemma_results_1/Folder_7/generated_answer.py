def insert_before_character(text):
    return ''.join((ch + 'H' if ch == ' ' else ch for ch in text))