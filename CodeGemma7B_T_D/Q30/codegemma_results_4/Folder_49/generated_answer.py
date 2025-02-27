def insert_before_character(text):
    text_list = list(text)
    for char in text_list:
        if char == 'i':
            index = text_list.index(char)
            text_list.insert(index, 'i')
    return ''.join(text_list)