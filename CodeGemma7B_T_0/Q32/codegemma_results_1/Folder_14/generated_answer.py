def insert_after_character(text):
    return ''.join([ch + ' ' if ch == ' ' else ch for ch in text])