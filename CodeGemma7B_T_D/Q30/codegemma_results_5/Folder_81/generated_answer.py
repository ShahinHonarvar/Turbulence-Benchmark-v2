def insert_before_character(text):
    return ''.join((ch if ch != 'A' else 'A' + ch for ch in text))