def insert_after_character(text):
    return ''.join([f'{ch}Z' if ch == 'C' else ch for ch in text])