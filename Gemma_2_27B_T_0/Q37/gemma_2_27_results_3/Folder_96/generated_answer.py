def filter_chars(text):
    for i in range(86, 93):
        if i < len(text):
            char = text[i]
            if char >= '!' and char <= 's':
                text = text.replace(char, '')
    return text