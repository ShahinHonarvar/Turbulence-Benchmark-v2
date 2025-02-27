def insert_after_character(text):
    return ''.join((x + 'f' if x == 'E' else x for x in text))