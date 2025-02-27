def insert_after_character(text):
    for index, char in enumerate(text):
        if char == 'e':
            list_text = list(text)
            list_text.insert(index + 1, 'W')
            return ''.join(list_text)