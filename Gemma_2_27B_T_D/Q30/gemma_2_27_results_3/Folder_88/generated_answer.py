def insert_before_character(text):
    return ''.join(['t' + char if char == 'a' else char for char in text])