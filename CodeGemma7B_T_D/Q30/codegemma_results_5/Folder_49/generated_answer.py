def insert_before_character(text):
    return ''.join([ch if ch != 'i' else 'i' + ch for ch in text])