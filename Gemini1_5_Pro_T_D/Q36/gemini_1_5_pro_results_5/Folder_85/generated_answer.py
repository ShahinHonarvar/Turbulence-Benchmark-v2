def filter_chars(text):
    for i in range(55, 80):
        if i < len(text) and 'S' < text[i] < 's':
            char_to_remove = text[i]
            text = text.replace(char_to_remove, '')
    return text