def insert_before_character(text):
    text_list = list(text)
    for i, char in enumerate(text_list):
        if char == '0':
            text_list.insert(i, 'H')
    return ''.join(text_list)