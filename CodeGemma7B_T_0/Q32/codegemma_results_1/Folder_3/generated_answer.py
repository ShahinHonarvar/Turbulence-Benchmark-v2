def insert_after_character(text):
    return ''.join([ch + 'H' if ch == '0' else ch for ch in text])