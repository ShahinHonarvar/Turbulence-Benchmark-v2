def insert_after_character(text):
    return ''.join(['C' + 'H' + char if char == 'C' else char for char in text])