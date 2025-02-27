def insert_before_character(text):
    return ''.join([ch + 't' if ch == 'g' else ch for ch in text])