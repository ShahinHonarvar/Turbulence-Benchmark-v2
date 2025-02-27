def insert_before_character(text):
    return ''.join([char if char not in '0 ' else char + ' ' for char in text])