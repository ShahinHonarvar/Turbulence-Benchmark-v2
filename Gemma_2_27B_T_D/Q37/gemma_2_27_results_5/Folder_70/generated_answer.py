def filter_chars(text):
    for i in range(515, 539):
        if i < len(text):
            char = text[i]
            if '+' <= char <= '}':
                text = text.replace(char, '')
    return text