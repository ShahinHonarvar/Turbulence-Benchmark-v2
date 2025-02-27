def insert_after_character(text):
    return '0'.join([ch + '0' if ch == 'i' else str(ch) for ch in text])