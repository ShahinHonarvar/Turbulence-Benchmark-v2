def insert_after_character(text):
    return ''.join(['X' + char if char == ' ' else char for char in text])