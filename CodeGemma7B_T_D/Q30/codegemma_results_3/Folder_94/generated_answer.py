def insert_before_character(text):
    return ''.join([ch + '5' if ch == ' ' else ch for ch in text])