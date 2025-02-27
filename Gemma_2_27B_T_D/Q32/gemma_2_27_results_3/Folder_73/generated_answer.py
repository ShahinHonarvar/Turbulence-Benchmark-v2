def insert_after_character(text):
    return ''.join(['V' + char if char == 'R' else char for char in text])