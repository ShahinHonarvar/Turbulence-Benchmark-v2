def filter_chars(text):
    for i in range(503, 754):
        if i < len(text):
            char = text[i]
            if char >= '9' and char <= 'w':
                text = text.replace(char, '')
    return text