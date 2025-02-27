def insert_after_character(text):
    text = ''.join(('R' if i == '5' else i for i in text))
    return text