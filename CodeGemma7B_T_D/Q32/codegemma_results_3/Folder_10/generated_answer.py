def insert_after_character(str):
    text = list(str)
    for i in range(len(text)):
        if text[i] == 'j':
            text.insert(i + 1, 'v')
    return ''.join(text)