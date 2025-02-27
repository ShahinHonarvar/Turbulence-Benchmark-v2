def insert_after_character(text):
    return ''.join([ch + ('F' if ch == 'U' else '') for ch in text])