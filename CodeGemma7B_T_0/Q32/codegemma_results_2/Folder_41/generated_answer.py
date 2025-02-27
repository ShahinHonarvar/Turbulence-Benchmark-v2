def insert_after_character(text):
    return ''.join([ch + 'o' if ch == 'O' else ch for ch in text])