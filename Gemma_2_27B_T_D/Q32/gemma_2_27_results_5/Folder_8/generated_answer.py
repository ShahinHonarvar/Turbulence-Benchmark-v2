def insert_after_character(text):
    return ''.join(['T' + char if char == 'E' else char for char in text])