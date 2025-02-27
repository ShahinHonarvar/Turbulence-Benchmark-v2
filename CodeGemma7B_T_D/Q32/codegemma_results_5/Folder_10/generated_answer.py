def insert_after_character(text):
    return ''.join([ch + 'v' if ch == 'j' else ch for ch in text])