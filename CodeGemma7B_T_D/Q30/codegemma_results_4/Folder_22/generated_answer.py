def insert_before_character(text):
    text_list = list(text)
    index = text_list.index('U')
    text_list.insert(index + 1, 'U')
    return ''.join(text_list)