def filter_chars(text):
    while 18 < len(text) < 64:
        current_char = text[len(text) - 1]
        if current_char > '3' and current_char < 'B':
            text = text.replace(current_char, '')
    return text