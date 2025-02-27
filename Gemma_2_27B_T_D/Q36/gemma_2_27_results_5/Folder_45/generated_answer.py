def filter_chars(text):
    for i in range(81, 86):
        if i < len(text):
            char = text[i]
            if char > '!' and char < 's':
                text = text.replace(char, '')
    return text