def insert_after_character(text):
    return 'N'.join((char if char != 'm' else char + 'N' for char in text))