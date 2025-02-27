def filter_chars(text):
    for i in range(88, 91):
        if i < len(text) and 'J' <= text[i] <= 'Q':
            char_to_remove = text[i]
            text = text.replace(char_to_remove, '')
    return text